import pathlib
from trademaskerfilewatcher.watcher import TradeMaskerFileWatcher
from trademaskerfilewatcher.processors.pdf_to_masked_text_processor import PdfToMaskedTextProcessor


def test_scan_once_processes_new_file(tmp_path):
    pdf = tmp_path / "statement.pdf"
    # A real PDF is not needed for this test, as the processor is mocked.
    # However, creating the file is important.
    pdf.touch()

    output = tmp_path / "masked"
    output.mkdir()

    class Dummy:
        def process(self, path, out):
            out_file = pathlib.Path(out) / "statement_masked.txt"
            out_file.write_text("MASKED")
            return str(out_file)

    watcher = TradeMaskerFileWatcher(
        {
            "watch_folder": str(tmp_path),
            "mask_output_folder": str(output),
            "file_pattern": "*.pdf",
            "poll_interval": 1,
        },
        Dummy(),
    )

    results = watcher.scan_once()
    assert len(results) == 1
    out_file = pathlib.Path(results[0])
    assert out_file.exists()
    assert out_file.suffix == ".txt"
    assert out_file.read_text() == "MASKED"
