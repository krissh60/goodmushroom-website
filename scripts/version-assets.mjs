// Run after editing shared CSS/JS and before verification/release.
import fs from 'node:fs';
import path from 'node:path';
import {createHash} from 'node:crypto';
const root=path.resolve(import.meta.dirname,'..');
const hashes=Object.fromEntries(['css/style.css','js/main.js','js/analytics.js'].map(f=>[f,createHash('sha256').update(fs.readFileSync(path.join(root,f))).digest('hex').slice(0,12)]));
function walk(d){return fs.readdirSync(d,{withFileTypes:true}).flatMap(e=>e.name.startsWith('.')||['advisory','node_modules'].includes(e.name)?[]:e.isDirectory()?walk(path.join(d,e.name)):[path.join(d,e.name)])}
for(const f of walk(root).filter(f=>f.endsWith('.html'))){
 const before=fs.readFileSync(f,'utf8');
 const after=before.replace(/((?:src|href)="\/?(?:\.\.\/)*(css\/style\.css|js\/(?:main|analytics)\.js))(?:\?v=[^"\s]+)?"/g,(_,start,asset)=>start+'?v='+hashes[asset]+'"');
 if(after!==before)fs.writeFileSync(f,after);
}
console.log('Versioned shared assets:',hashes);
