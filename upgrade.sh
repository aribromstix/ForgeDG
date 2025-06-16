#!/usr/bin/env bash
set -e
# Usuń stare wstrzyknięcia
sed -i '/# BEGIN AUTO-CMDS/,/# END AUTO-CMDS/d' cli.py
# Wstaw nowe komendy
cat << 'EOF2' >> cli.py
# BEGIN AUTO-CMDS
EOF2
for cmd in templates/commands/*.py; do
  sed 's/^/    /' "$cmd" >> cli.py
  echo >> cli.py
done
cat << 'EOF2' >> cli.py
# END AUTO-CMDS
EOF2
# Przeładuj CLI
pip install -e .
echo "upgrade.sh: komendy zaktualizowane."
