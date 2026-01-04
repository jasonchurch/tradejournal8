import pdfplumber

def extract_text(pdf_path: str) -> str:
    text_parts = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text_parts.append(page.extract_text() or "")
    return "\n".join(text_parts)

text = extract_text("/home/red0ck33g/Downloads/Confirmation_19RW78J_03-Feb-25_2.pdf")
print(text)