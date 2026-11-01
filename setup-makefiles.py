#!/bin/bash
set -e
MY_DIR="$(cd "$(dirname "${0}")"; pwd -P)"
DEVICE="${1:-}"
if [[ ! "$DEVICE" =~ ^(akita|husky|shiba)$ ]]; then
    echo "Usage: $0 {akita|husky|shiba}" >&2
    exit 2
fi
exec "$MY_DIR/$DEVICE/setup-makefiles.py"
