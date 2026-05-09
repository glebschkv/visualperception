#!/bin/bash
# Extract text from all PDFs into one combined file using pdftotext.
set -e
cd "$(dirname "$0")"
OUT="all_pdfs.txt"
: > "$OUT"
echo "# Combined text extracted from PDFs in $(pwd)" >> "$OUT"
echo "" >> "$OUT"

for pdf in *.pdf; do
  echo "Extracting: $pdf" >&2
  {
    echo ""
    printf '=%.0s' {1..80}; echo
    echo "FILE: $pdf"
    printf '=%.0s' {1..80}; echo
    echo ""
  } >> "$OUT"
  pdftotext -layout "$pdf" - >> "$OUT" 2>/dev/null || echo "[ERROR extracting $pdf]" >> "$OUT"
done

bytes=$(wc -c < "$OUT")
words=$(wc -w < "$OUT")
echo "Wrote $OUT — ${bytes} bytes, ${words} words (~$((words * 4 / 3)) tokens approx)" >&2
