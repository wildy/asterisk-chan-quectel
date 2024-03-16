#!/bin/bash
set -euo pipefail
if [ ! -c /dev/quectel0-data ] || [ ! -c /dev/quectel0-audio ]; then
  echo "No Quectel devices detected; failing."
  exit 1
fi

/usr/sbin/asterisk -rx "quectel show device state quectel0"
