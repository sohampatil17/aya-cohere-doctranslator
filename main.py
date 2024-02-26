import cohere
import fitz
from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_font('Hindi', '', 'AnnapurnaSIL-Regular.ttf', uni=True)

    def header(self):
        self.set_font('Arial','I',10)
        self.cell(0, 10, 'Translated using SahayakAI', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

def aya_translation(input_text, cohere_api_key):
    co = cohere.Client(cohere_api_key)  # This is your trial API key
    fix_prompt = 'Translate and finish this letter for me in Hindi while maintaining the format in output text:'
    end_prompt = 'Ensure your output translation is in Hindi language'
    response = co.generate(
        model='c4ai-aya',
        prompt=fix_prompt + input_text + end_prompt,
        max_tokens=3000,
        temperature=0.9,
        k=0,
        stop_sequences=[],
        return_likelihoods='NONE')
    return response.generations[0].text

def save_text_to_pdf(text, filename):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Hindi', '', 14)
    pdf.set_auto_page_break(auto=True, margin=5)  # Set auto page break

    # Split the text into lines
    lines = text.split('\n')
    for line in lines:
        pdf.cell(0, 10, line, ln=1, align='L')  # Use cell with ln=1 for automatic new lines

    pdf.output(filename)

def process_pdf(file_path, cohere_api_key):
    text = extract_text(file_path)
    hindi_translation = aya_translation(text, cohere_api_key)
    output_pdf_path = 'translated_output.pdf'
    save_text_to_pdf(hindi_translation, output_pdf_path)
    return output_pdf_path


