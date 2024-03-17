#!/bin/bash
set -euo pipefail

STATE="$(/usr/sbin/asterisk -rx "quectel show device state quectel0"|grep State)"

[[ "$STATE" =~ 'Not connected' ]] && exit 1 || exit 0