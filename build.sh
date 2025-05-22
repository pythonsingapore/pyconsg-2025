#!/usr/bin/env bash
set -euo pipefail

PAGES=('index.html' 'archive.html' 'sponsor.html' 'team.html' 'edusummit.html' 'speakers.html' 'about.html')

echo "Regenerating pages..."
cd src/
for page in "${PAGES[@]}"; do
  echo "  ${page}"
  cat header.html navbar.html "${page}" footer.html > "../${page}"
done

cd ..
echo "Done!"
