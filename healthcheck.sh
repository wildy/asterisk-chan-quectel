#!/bin/bash
set -euo pipefail

STATE="$(/usr/sbin/asterisk -rx "quectel show device state quectel0"|grep GSM Registration Status)"

[[ "$STATE" =~ 'Registered' ]] && exit 1 || exit 0
