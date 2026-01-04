import argparse
import yaml
from trademaskerfilewatcher.watcher import TradeMaskerFileWatcher
from trademaskerfilewatcher.processors.pdf_to_masked_text_processor import PdfToMaskedTextProcessor


def main():
    parser = argparse.ArgumentParser(description="Trade Masker File Watcher")
    parser.add_argument("--config", required=True, help="Path to YAML config file")
    args = parser.parse_args()

    with open(args.config) as f:
        config = yaml.safe_load(f)

    masking_patterns = config.get("masking_patterns", [])
    processor = PdfToMaskedTextProcessor(patterns_to_mask=masking_patterns)
    watcher = TradeMaskerFileWatcher(config, processor)
    watcher.run()


if __name__ == "__main__":
    main()