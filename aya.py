import cohere
import fitz
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

pdf_text = extract_text('offer-letter.pdf')

cohere_api=''
co = cohere.Client(cohere_api) # This is your trial API key

fix_prompt = 'Translate and finish this letter for me in Hindi: '
input_text = pdf_text

response = co.generate(
    model='c4ai-aya',
    prompt = fix_prompt + input_text,
    max_tokens=3000,
    temperature=0.9,
    k=0,
    stop_sequences=[],
    return_likelihoods='NONE')

hindi_translation = response.generations[0].text

with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(hindi_translation)

print("Done")