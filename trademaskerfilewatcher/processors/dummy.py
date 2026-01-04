import pathlib


class DummyMasker:
    def process(self, path: str, output_dir: str) -> str:
        pdf_path = pathlib.Path(path)
        out_path = pathlib.Path(output_dir) / f"{pdf_path.stem}_masked.pdf"
        print(f"[DummyMasker] Masking {pdf_path} → {out_path}")
        out_path.write_text("MASKED CONTENT")
        return str(out_path)
