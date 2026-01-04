import pathlib
import time
from typing import Protocol


class PdfProcessor(Protocol):
    def process(self, path: str, output_dir: str) -> str: ...


class TradeMaskerFileWatcher:
    def __init__(self, config: dict, processor: PdfProcessor):
        self.watch_folder = pathlib.Path(config["watch_folder"])
        self.output_folder = pathlib.Path(config["mask_output_folder"])
        self.file_pattern = config.get("file_pattern", "*.pdf")
        self.poll_interval = config.get("poll_interval", 2)
        self.processor = processor
        self.seen_files = set()
        self.output_folder.mkdir(parents=True, exist_ok=True)

    def scan_once(self):
        """Scan the folder once and process any new PDFs."""
        results = []
        for pdf in self.watch_folder.glob(self.file_pattern):
            if pdf not in self.seen_files:
                try:
                    result = self.processor.process(str(pdf), str(self.output_folder))
                    results.append(result)
                    self.seen_files.add(pdf)
                except Exception as e:
                    raise RuntimeError(f"Error processing {pdf}: {e}")
        return results

    def run(self):
        print(f"Watching {self.watch_folder} for {self.file_pattern} ...")
        while True:
            self.scan_once()
            time.sleep(self.poll_interval)