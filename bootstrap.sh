#!/usr/bin/env bash
set -e
echo "== Instalacja developerska =="
pip install -e .
echo "== Upgrade komend =="
./upgrade.sh
echo "== Generowanie CI/CD i Docker =="
forge init-ci
forge dockerize
echo "== Progress logging =="
forge init-progress
forge log-progress "Bootstrap: komendy załadowane"
echo "== Zabezpieczenia =="
# forge init-license --type MIT
forge init-legal
forge init-secrets
echo "== Gotowe: lista komend =="
forge --help
