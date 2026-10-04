#!/data/data/com.termux/files/usr/bin/bash
set -e
ROOT="$(cd "$(dirname "$0")" && pwd)"
chmod +x "$ROOT/blacktrace.py"
mkdir -p "$PREFIX/bin"
cat > "$PREFIX/bin/blacktrace" <<EOF
#!/data/data/com.termux/files/usr/bin/bash
exec python3 "$ROOT/blacktrace.py" "\$@"
EOF
chmod +x "$PREFIX/bin/blacktrace"
echo "BLACKTRACE installed. Run: blacktrace"
