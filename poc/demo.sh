#!/usr/bin/env bash
# FORGEDG POC Demo Script

set -e

# 1. Uruchom API (w tle)
echo "Uruchamiam API..."
cd ../white-label/api
source venv/bin/activate
nohup ./run.sh > ../../poc/api.log 2>&1 &

# 2. Uruchom Web-Demo
echo "Uruchamiam Web-Demo..."
cd ../www
nohup python3 -m http.server 8000 > ../../poc/web-demo.log 2>&1 &

sleep 2

# 3. Wysyłka testowego pliku
TEST_URL="https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv"
echo "Wysyłam testowy plik: $TEST_URL"
RESPONSE=$(curl -s -X POST http://localhost:5000/process \
  -H "Content-Type: application/json" \
  -d "{\"fileUrl\":\"$TEST_URL\"}")
JOBID=$(echo $RESPONSE | sed -E 's/.*"jobId":"([^"]+)".*/\1/')
echo "Otrzymane jobId: $JOBID"

# 4. Sprawdzenie statusu
sleep 1
STATUS=$(curl -s "http://localhost:5000/status?jobId=$JOBID" | sed -E 's/.*"status":"([^"]+)".*/\1/')
echo "Aktualny status: $STATUS"

echo "POC zakończony."
