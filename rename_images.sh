#!/bin/bash

# Set the directory (current directory)
DIR="camera_uploads"

# Initialize counter
COUNT=1

# Loop through all files in the directory
for FILE in "$DIR"/*; do
  if [ -f "$FILE" ]; then
    NEWNAME="$DIR/conky$COUNT.png"
    mv "$FILE" "$NEWNAME"
    ((COUNT++))
  fi
done
