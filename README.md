# SahayakAI - PDF Translation Tool

SahayakAI is a Python-based tool that utilizes the Cohere API to translate the contents of PDF documents into Hindi, maintaining the original format. It uses Streamlit for a simple web interface that allows users to upload a PDF, view the original and the translated document, and download the translated version.

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




