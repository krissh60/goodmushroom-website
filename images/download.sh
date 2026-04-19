#!/bin/bash
# Good Mushroom — download real product photography from Pexels (free, no attribution required for commercial use — Pexels license).
# Run from the site root:  bash images/download.sh
# Replace any of these with your own product photography once available.
set -e
cd "$(dirname "$0")"

# Format: curl -L -o <local name> "<Pexels/Unsplash URL>"
# Pexels CDN pattern: https://images.pexels.com/photos/<ID>/pexels-photo-<ID>.jpeg?auto=compress&cs=tinysrgb&w=1200

# Hero / About visual
curl -sL -o hero.jpg         "https://images.pexels.com/photos/1108701/pexels-photo-1108701.jpeg?auto=compress&cs=tinysrgb&w=1800"
curl -sL -o about.jpg        "https://images.pexels.com/photos/7728678/pexels-photo-7728678.jpeg?auto=compress&cs=tinysrgb&w=1200"

# Products (800x800 square crops)
curl -sL -o cordyceps.jpg    "https://images.pexels.com/photos/4750274/pexels-photo-4750274.jpeg?auto=compress&cs=tinysrgb&w=800"
curl -sL -o shiitake.jpg     "https://images.pexels.com/photos/1640774/pexels-photo-1640774.jpeg?auto=compress&cs=tinysrgb&w=800"
curl -sL -o lions-mane.jpg   "https://images.pexels.com/photos/7936616/pexels-photo-7936616.jpeg?auto=compress&cs=tinysrgb&w=800"
curl -sL -o oyster.jpg       "https://images.pexels.com/photos/5946081/pexels-photo-5946081.jpeg?auto=compress&cs=tinysrgb&w=800"
curl -sL -o reishi.jpg       "https://images.pexels.com/photos/6823568/pexels-photo-6823568.jpeg?auto=compress&cs=tinysrgb&w=800"
curl -sL -o button.jpg       "https://images.pexels.com/photos/1028599/pexels-photo-1028599.jpeg?auto=compress&cs=tinysrgb&w=800"
curl -sL -o extract.jpg      "https://images.pexels.com/photos/5946080/pexels-photo-5946080.jpeg?auto=compress&cs=tinysrgb&w=800"
curl -sL -o herbs.jpg        "https://images.pexels.com/photos/4021687/pexels-photo-4021687.jpeg?auto=compress&cs=tinysrgb&w=800"

# OG social image (1200x630)
curl -sL -o og-image.jpg     "https://images.pexels.com/photos/1108701/pexels-photo-1108701.jpeg?auto=compress&cs=tinysrgb&w=1200&h=630&fit=crop"

echo ""
echo "✅ Downloaded $(ls -1 *.jpg 2>/dev/null | wc -l | tr -d ' ') images."
echo ""
echo "Preview locally:  python3 -m http.server 8000"
echo "Replace any of these with real product photography whenever available —"
echo "filenames are what the HTML references."
