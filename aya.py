import cohere
import fitz
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors

pdfmetrics.registerFont(TTFont('HindiFont', 'AnnapurnaSIL-Regular.ttf'))

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

pdf_text = extract_text('offer-letter.pdf')

cohere_api='U4YiqSDHIkdFIItNWEwLVA7nLQ1aQm2HCyUmdu6h'
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

def save_text_to_pdf(text, filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter  # Get the dimensions of the page
    margin = 40  # Margin for the page
    max_height = height - 2 * margin
    text_object = c.beginText(margin, height - margin)  # Start below the top margin
    text_object.setFont('HindiFont', 12)

    for paragraph in text.split('\n'):
        words = paragraph.split()
        line = ''
        for word in words:
            # Check if adding the next word would exceed the line width
            if pdfmetrics.stringWidth(line + ' ' + word, 'HindiFont', 12) <= (width - 2 * margin):
                line += ' ' + word if line else word
            else:
                # Add the line to the canvas if the next word would exceed the line width
                text_object.textLine(line)
                line = word
                # Check to see if we are at the end of the page
                if text_object.getY() <= margin + 15:  # 15 is the line height
                    # We are at the bottom of the page, so let's create a new page
                    c.drawText(text_object)
                    c.showPage()
                    text_object = c.beginText(margin, height - margin)
                    text_object.setFont('HindiFont', 12)

        # Add the last line of the paragraph if it's not empty
        if line:
            text_object.textLine(line)
            line = ''
        # Add some space after a paragraph, check for page end here too
        if text_object.getY() <= margin + 15:
            c.drawText(text_object)
            c.showPage()
            text_object = c.beginText(margin, height - margin)
            text_object.setFont('HindiFont', 12)
        else:
            text_object.moveCursor(0, 15)  # This is the space between paragraphs

    # Don't forget to draw the last piece of text
    c.drawText(text_object)
    c.save()

save_text_to_pdf(hindi_translation, 'translated_output.pdf')
print("Done")