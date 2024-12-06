#!/bin/bash

# Source and destination directories
SRC="assets/icons/logo.png"
DEST="static/favicons"

# Create destination directory if it doesn't exist
mkdir -p "$DEST"

# Generate Android icons
magick "$SRC" -resize 36x36 "$DEST/android-36x36.png"
magick "$SRC" -resize 48x48 "$DEST/android-48x48.png"
magick "$SRC" -resize 72x72 "$DEST/android-72x72.png"
magick "$SRC" -resize 96x96 "$DEST/android-96x96.png"
magick "$SRC" -resize 144x144 "$DEST/android-144x144.png"
magick "$SRC" -resize 192x192 "$DEST/android-192x192.png"

# Generate Apple icon
magick "$SRC" -resize 180x180 "$DEST/apple-touch-icon-180x180.png"

# Generate various favicon sizes
magick "$SRC" -resize 16x16 "$DEST/favicon-16x16.png"
magick "$SRC" -resize 32x32 "$DEST/favicon-32x32.png"
magick "$SRC" -resize 256x256 "$DEST/favicon-256.png"
magick "$SRC" -resize 1024x1024 "$DEST/favicon-1024.png"

# Generate PWA icons
magick "$SRC" -resize 192x192 "$DEST/pwa-192x192.png"
magick "$SRC" -resize 512x512 "$DEST/pwa-512x512.png"

# Generate Windows tiles
magick "$SRC" -resize 70x70 "$DEST/tile70x70.png"
magick "$SRC" -resize 150x150 "$DEST/tile150x150.png"
magick "$SRC" -resize 310x150 "$DEST/tile310x150.png"
magick "$SRC" -resize 310x310 "$DEST/tile310x310.png"

# Generate .ico file (contains multiple sizes)
magick "$SRC" -resize 16x16 "$SRC" -resize 32x32 "$SRC" -resize 48x48 "$DEST/favicon.ico"

echo "All favicons have been generated in $DEST"
