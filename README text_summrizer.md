# Text Summarizer Web App

> An AI-powered web application that extracts and summarizes text from PDFs, images, and plain-text files using state-of-the-art NLP models.

---

## Overview

**Text Summarizer Web App** is a full-stack Python + Flask project that accepts file uploads through a browser interface and returns concise, AI-generated summaries. It supports multi-format input, combining OCR technology with transformer-based summarization to handle everything from scanned images to academic PDFs.

This project was built to demonstrate practical integration of machine learning pipelines into a production-ready web API.

---

## Features

- **Multi-format Support** — Summarize content from `.pdf`, `.txt`, `.jpg`, `.jpeg`, and `.png` files
- **OCR Pipeline** — Extracts text from images using Tesseract OCR via `pytesseract`
- **PDF Parsing** — Reads native PDF text layer using `PyMuPDF (fitz)`
- **AI Summarization** — Powered by Hugging Face `facebook/bart-large-cnn` transformer model
- **REST API** — Clean `/upload` endpoint returns structured JSON responses
- **Web Interface** — Minimal browser-based frontend for quick file upload and summary display

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| NLP / AI | Hugging Face Transformers (`facebook/bart-large-cnn`) |
| OCR | Tesseract OCR, pytesseract |
| PDF Parsing | PyMuPDF (fitz) |
| Image Processing | Pillow, OpenCV |
| Frontend | HTML, JavaScript (Fetch API) |

---

## Project Structure

```
text_summarizer_web/
├── app.py              # Flask app and /upload API route
├── summarizer.py       # Core extraction and summarization logic
├── summ2.py            # CLI-based standalone summarizer script
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Frontend upload interface
└── static/             # Static assets directory
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed and added to your system PATH

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/text_summarizer_web.git
cd text_summarizer_web

# 2. Create and activate a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt
```

### Running the Web App

```bash
python app.py
```

Then open your browser and go to `http://127.0.0.1:5000`.

### Running the CLI Summarizer

```bash
python summ2.py path/to/your/file.pdf
```

Supports `.pdf`, `.txt`, `.jpg`, `.jpeg`, `.png`.

---

## API Reference

### POST `/upload`

Upload a file and receive a summary.

**Request** — `multipart/form-data`

| Field | Type | Description |
|---|---|---|
| `file` | File | The document or image to summarize |

**Response** — `application/json`

```json
{
  "summary": "A concise AI-generated summary of the uploaded content."
}
```

---

## How It Works

```
User uploads file
      |
      v
File type detected (.pdf / .txt / .jpg / .png)
      |
      |---> PDF  --> PyMuPDF extracts native text
      |---> Image --> Tesseract OCR extracts text
      |---> TXT  --> Direct file read
      |
      v
Text cleaned and passed to Hugging Face pipeline
      |
      v
facebook/bart-large-cnn generates abstractive summary
      |
      v
Summary returned as JSON response
```

---

## Dependencies

```
flask
PyMuPDF
pytesseract
Pillow
opencv-python
numpy
transformers
```

Install all with:

```bash
pip install -r requirements.txt
```

---

## What I Learned

- Integrating pre-trained Hugging Face transformer models into a Python backend
- Building multi-format file processing pipelines (OCR + native text extraction)
- Designing REST APIs with Flask for ML inference tasks
- Handling binary file uploads securely with `werkzeug`

---

## Future Improvements

- Add support for `.docx` (Word documents)
- Add summary length control via frontend slider
- Deploy on Render / Hugging Face Spaces
- Add drag-and-drop file upload UI
- Implement streaming responses for faster perceived performance

---

## Author

**Preet**
- GitHub: [@your-username](https://github.com/your-username)
- Portfolio: [your-portfolio-link.com](https://your-portfolio-link.com)
- LinkedIn: [linkedin.com/in/your-profile](https://linkedin.com/in/your-profile)

---

## License

This project is open source and available under the [MIT License](LICENSE).
