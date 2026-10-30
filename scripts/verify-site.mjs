// Dependency-free release checks for the main domain. Advisory is a separate site.
import fs from 'node:fs';
import path from 'node:path';
import {createHash} from 'node:crypto';
const root=path.resolve(import.meta.dirname,'..');
const errors=[];let links=0,schemas=0;
const check=(ok,message)=>{if(!ok)errors.push(message)};
function walk(d){return fs.readdirSync(d,{withFileTypes:true}).flatMap(e=>e.name.startsWith('.')||['advisory','node_modules'].includes(e.name)?[]:e.isDirectory()?walk(path.join(d,e.name)):[path.join(d,e.name)])}
const files=walk(root).filter(f=>f.endsWith('.html'));
const pages=new Map(files.map(f=>[f,fs.readFileSync(f,'utf8')]));
const decode=s=>s.replace(/&amp;/g,'&').replace(/&#x27;|&#39;|&apos;/g,"'").replace(/&quot;/g,'"');
const titles=new Set();const canonicals=new Set();
for(const [f,s] of pages){
 const rel=path.relative(root,f).replaceAll('\\','/');
 const count=re=>[...s.matchAll(re)].length;
 check(count(/<h1\b/gi)===1,rel+': expected one H1');
 check(count(/<body\b/gi)===1,rel+': expected one body');
 const title=s.match(/<title>([^<]+)<\/title>/i)?.[1];
 check(title&&!titles.has(title),rel+': missing/duplicate title');titles.add(title);
 check(/<meta name="description" content="[^"]+"/i.test(s),rel+': missing description');
 const canonical=s.match(/<link rel="canonical" href="([^"]+)"/i)?.[1];
 const expected='https://goodmushroom.in/'+(rel==='index.html'?'':rel);
 check(canonical===expected&&!canonicals.has(canonical),rel+': canonical mismatch');canonicals.add(canonical);
 check(rel==='404.html'||!/<meta name="robots"[^>]+noindex/i.test(s),rel+': unexpected noindex');
 const ids=[...s.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]);
 check(ids.length===new Set(ids).size,rel+': duplicate ids');
 for(const m of s.matchAll(/<label\b[^>]*for="([^"]+)"/g))check(ids.includes(m[1]),rel+': broken label '+m[1]);
 for(const m of s.matchAll(/<(?:input|select|textarea)\b([^>]*)>/g)){
  const attrs=m[1];if(/type="(?:hidden|submit|button)"|name="website"/.test(attrs))continue;
  const id=attrs.match(/\bid="([^"]+)"/)?.[1];
  check(/aria-label=/.test(attrs)||(id&&s.includes('for="'+id+'"')),rel+': unlabelled form control '+(attrs.match(/name="([^"]+)"/)?.[1]||'unknown'));
 }
 for(const m of s.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)){
  try{JSON.parse(m[1]);schemas++}catch{errors.push(rel+': invalid JSON-LD')}
 }
 if(rel!=='404.html')check(count(/src="(?:\.\.\/)*js\/analytics\.js\?v=/g)===1,rel+': expected shared analytics once');
 check(!/googletagmanager|G-3JPKHJHFQM/.test(s),rel+': inline analytics must use shared initializer');
 for(const m of s.matchAll(/\b(?:href|src)="([^"]+)"/g)){
  const raw=decode(m[1]);if(/^(?:https?:|mailto:|tel:|data:|javascript:)/i.test(raw))continue;
  const url=new URL(raw,'https://goodmushroom.in/'+rel);
  const local=path.join(root,decodeURIComponent(url.pathname)==='/'?'index.html':decodeURIComponent(url.pathname));
  if(url.pathname.startsWith('/advisory/'))continue;
  links++;check(fs.existsSync(local),rel+': missing local resource '+raw);
  if(url.hash&&pages.has(local))check(pages.get(local).includes('id="'+decodeURIComponent(url.hash.slice(1))+'"'),rel+': missing fragment '+raw);
  if(/(?:css\/style\.css|js\/(?:main|analytics)\.js)$/.test(url.pathname)&&fs.existsSync(local)){
   const hash=createHash('sha256').update(fs.readFileSync(local)).digest('hex').slice(0,12);
   check(url.searchParams.get('v')===hash,rel+': stale asset version '+raw);
  }
 }
 for(const m of s.matchAll(/<a\b([^>]*)>/g)){
  const a=m[1],action=a.match(/data-track="([^"]+)"/)?.[1];if(!action)continue;
  check(['ingredient','quote','specifications','supplier','whatsapp'].includes(action),rel+': invalid action');
  if(action==='ingredient')check(/data-product="[a-z-]+"/.test(a),rel+': ingredient missing product ID');
  if(rel.startsWith('products/')&&['quote','specifications'].includes(action)&&/contact\.html/.test(a))check(/\?product=[a-z-]+/.test(a),rel+': CTA lost product context');
 }
}
const sitemap=fs.readFileSync(path.join(root,'sitemap.xml'),'utf8');
const urls=[...sitemap.matchAll(/<loc>([^<]+)<\/loc>/g)].map(m=>m[1]);
check(urls.length===new Set(urls).size,'Sitemap has duplicate URLs');
for(const url of urls)check(canonicals.has(url),'Sitemap URL lacks canonical page: '+url);
for(const url of canonicals)if(!url.endsWith('/404.html'))check(urls.includes(url),'Canonical absent from sitemap: '+url);
console.log(JSON.stringify({pages:files.length,sitemapUrls:urls.length,localReferences:links,jsonLdBlocks:schemas,errors},null,2));
if(errors.length)process.exitCode=1;
