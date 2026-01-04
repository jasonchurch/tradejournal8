import pathlib
import re
import pdfplumber


class PdfToMaskedTextProcessor:
    """
    A processor that extracts text from a PDF, masks sensitive information,
    and saves the result as a .txt file.
    """

    def __init__(self, patterns_to_mask: list[str]):
        # We compile the regex patterns for efficiency if this processor is used multiple times.
        self.compiled_patterns = [re.compile(p) for p in patterns_to_mask]

    def process(self, path: str, output_dir: str) -> str:
        """
        Processes a single PDF file.

        Args:
            path: The full path to the input PDF file.
            output_dir: The directory where the masked text file will be saved.

        Returns:
            The path to the newly created masked text file.
        """
        pdf_path = pathlib.Path(path)
        with pdfplumber.open(pdf_path) as pdf:
            text = "\n".join(page.extract_text() or "" for page in pdf.pages)

        for pattern in self.compiled_patterns:
            text = pattern.sub("****MASKED****", text)

        output_path = pathlib.Path(output_dir) / f"{pdf_path.stem}_masked.txt"
        output_path.write_text(text)
        return str(output_path)