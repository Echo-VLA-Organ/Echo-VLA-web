#!/usr/bin/env python3
"""Render PDF figures to PNG for the project page (use pypdfium2, not PyMuPDF)."""

from __future__ import annotations

import argparse
from pathlib import Path

import pypdfium2 as pdfium

DEFAULTS = [
    ("framework.pdf", "framework.png", 3),
    ("gen_pipeline.pdf", "gen_pipeline.png", 2),
    ("data_statics.pdf", "data_statics.png", 3),
]


def convert(pdf_path: Path, png_path: Path, scale: int) -> None:
    doc = pdfium.PdfDocument(str(pdf_path))
    try:
        page = doc[0]
        image = page.render(scale=scale, rotation=0).to_pil()
        image.save(png_path, format="PNG", optimize=True)
    finally:
        doc.close()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--images-dir",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "static" / "images",
    )
    args = parser.parse_args()
    for pdf_name, png_name, scale in DEFAULTS:
        pdf = args.images_dir / pdf_name
        png = args.images_dir / png_name
        convert(pdf, png, scale)
        print(f"{png_name} <- {pdf_name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
