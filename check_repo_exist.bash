#!/bin/bash

IMAGE_FILE="image_list.txt"

while IFS= read -r image; do
    if [ -z "$image" ]; then
        continue
    fi
    echo "Checking $image ..."
    if docker buildx imagetools inspect "$image" > /dev/null 2>&1; then
        echo "✅ Exists: $image"
    else
        echo "❌ Not found: $image"
    fi
done < "$IMAGE_FILE"
