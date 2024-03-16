#!/bin/bash
set -euo pipefail
/opt/scripts/modeminit.py
/usr/sbin/asterisk -f -n -Uasterisk -Gdialout
