#!/usr/bin/env python3
"""Extract text from all PDFs in this directory into one combined .txt file."""
import os
import sys
from pathlib import Path
from pypdf import PdfReader

HERE = Path(__file__).parent
OUT = HERE / "all_pdfs.txt"

pdfs = sorted(HERE.glob("*.pdf"))

with OUT.open("w", encoding="utf-8") as out:
    out.write(f"# Combined text extracted from {len(pdfs)} PDFs\n\n")
    for pdf in pdfs:
        print(f"Extracting {pdf.name}...", file=sys.stderr)
        out.write("\n" + "=" * 80 + "\n")
        out.write(f"FILE: {pdf.name}\n")
        out.write("=" * 80 + "\n\n")
        try:
            reader = PdfReader(str(pdf))
            for i, page in enumerate(reader.pages, 1):
                text = page.extract_text() or ""
                out.write(f"\n--- Page {i} ---\n{text}\n")
        except Exception as e:
            out.write(f"[ERROR extracting {pdf.name}: {e}]\n")

size = OUT.stat().st_size
print(f"\nWrote {OUT} ({size:,} bytes, ~{size//4:,} tokens approx)", file=sys.stderr)
