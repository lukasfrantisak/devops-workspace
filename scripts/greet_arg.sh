#!/bin/bash

JMENO=$1

if [ -z "$JMENO" ]; then
  echo "Nezadal jsi jméno. Použití: ./greet_arg.sh [tvoje_jmeno]"
  exit 1
fi

echo "Nazdar, $JMENO!"
echo "Dnes je: $(date)"
