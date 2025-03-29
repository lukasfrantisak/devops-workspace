#!/bin/bash

JMENO=$1
TEMA=$2

if [ -z "$JMENO" ] || [ -z "$TEMA" ]; then
  echo "Použití: ./pozdrav.sh [jméno] [téma]"
  exit 1
fi

echo "Nazdar $JMENO! Tak co, připraven na $TEMA?"