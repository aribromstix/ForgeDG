#!/usr/bin/env bash
# FORGEDG White-Label Install Script (Linux)

set -e

echo "1) Tworzę virtualenv dla API..."
python3 -m venv api/venv
echo "2) Aktywuję virtualenv i instaluję Flask..."
source api/venv/bin/activate
pip install --upgrade pip
pip install -r api/requirements.txt
deactivate

echo "3) Kopiuję web-demo do docroot..."
mkdir -p www
cp -r web-demo/* www/

echo "4) Tworzę plik README z instrukcjami..."
cat > README.txt << INSTR
FORGEDG White-Label Package

1. API:
   cd api
   source venv/bin/activate
   ./run.sh

2. Web-Demo:
   cd ../www
   python3 -m http.server 8000

INSTR

echo "Gotowe! Zobacz README.txt dla dalszych instrukcji."
