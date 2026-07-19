#!/usr/bin/env bash
# Downloads replacement stock images for hero (mushroom farm) and herbs (ashwagandha roots).
# Run on VPS or laptop with internet access:
#   bash scripts/swap-images.sh
#
# All photos are free-license from Unsplash (no attribution required for commercial use).

set -euo pipefail

cd "$(dirname "$0")/.."
mkdir -p images

# ---- HERO: replace mount-fuji-looking image with a real mushroom cultivation photo ----
# Photo: Andrew Ridley — mushrooms growing on log (free Unsplash license)
HERO_URL="https://images.unsplash.com/photo-1607301406259-dfb186e15de8?w=1800&q=80&fm=jpg"

# ---- HERBS: replace generic capsules/powder with actual ashwagandha roots on wood ----
# Photo: Aleksandra Boguslawska — dried roots & herbs (free Unsplash license)
HERBS_URL="https://images.unsplash.com/photo-1611071536243-cf8b3af5a09b?w=1800&q=80&fm=jpg"

echo "Downloading hero image..."
curl -fsSL -o images/hero.jpg "$HERO_URL"

echo "Downloading herbs image..."
curl -fsSL -o images/herbs.jpg "$HERBS_URL"

# Also regenerate WebP versions if cwebp is available, otherwise just copy JPG
if command -v cwebp >/dev/null 2>&1; then
  echo "Converting to WebP..."
  cwebp -q 82 images/hero.jpg  -o images/hero.webp
  cwebp -q 82 images/herbs.jpg -o images/herbs.webp
else
  echo "cwebp not installed — installing webp package would speed pages. For now, copying JPG as fallback."
  # Simpler: just delete the webp so <picture> falls back to jpg
  rm -f images/hero.webp images/herbs.webp
fi

echo ""
echo "Done. New images:"
ls -la images/hero.* images/herbs.*
echo ""
echo "Preview locally by opening images/hero.jpg and images/herbs.jpg."
echo "If you like them, commit and push:"
echo "  git add images/hero.* images/herbs.*"
echo "  git commit -m 'Replace hero and herbs images with real photography'"
echo "  git push"
