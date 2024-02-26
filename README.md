# SahayakAI - PDF Translation Tool

SahayakAI is an AI-driven software tool designed to transform the way legal documents are translated and understood in India. Legal documents in India are predominantly in English, which presents a formidable challenge in legal understanding and literacy for the vast majority of the population. Recognizing that over 90% of the Indian population speaks languages other than English, with a majority of 340M+ being native Hindi speakers, SahayakAI seeks to bridge the significant language barrier in legal contexts. The existing solutions, such as human translators and generic translation software, have notable limitations ranging from being too expensive to or lack of understanding of legal terminologies. To solve this, I built an AI solution that translates English 'legalese' into Hindi within seconds! We use Cohere's state-of-the-art multilingual AI model Aya to achieve this. Aya's advanced understanding of both English and Hindi ensures that the translations provided by SahayakAI maintain the integrity and intent of the original legal documents. Language translation services is a $40B+ global market on the brink of disruption due to multilingual LLMs like Aya.


## Features

- PDF text extraction.
- Translation to Hindi using Cohere's `c4ai-aya` model.
- PDF rendering with Hindi font support.
- Streamlit web interface for easy interaction.
- Header and footer customization in translated PDF.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher.
- Streamlit.
- Cohere API key.
- `fitz` (PyMuPDF) for reading PDFs.
- `fpdf2` for generating PDFs.

## Usage

To start the streamlit web app, 
streamlit run app.py

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/sahayakai.git
cd sahayakai
pip install -r requirements.txt




