#!/bin/bash

JMENO=$1
TEMA=$2
CAS=$(date)

if [ -z "$JMENO" ] || [ -z "$TEMA" ]; then
  echo "Použití: ./pozdrav_log.sh [jméno] [téma]"
  exit 1
fi

ZPRAVA="[$CAS] Nazdar $JMENO! Tak co, připraven na $TEMA?"

echo "$ZPRAVA"
echo "$ZPRAVA" >> pozdrav.log
