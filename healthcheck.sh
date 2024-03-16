#!/bin/bash
set -euo pipefail
/usr/sbin/asterisk -rx "quectel show device state quectel0"
