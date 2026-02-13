# AI-Based Medical Report Summarizer

This project is a FastAPI-based backend system that summarizes medical reports using a trained transformer model.

## Features
- REST API using FastAPI
- Transformer-based summarization
- Clean modular architecture
- Docker support

## Project Structure
- app/ → API logic
- model/ → Trained AI model
- requirements.txt → Dependencies
- Dockerfile → Containerization

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Run server:
   uvicorn app.main:app --reload

3. Open:
   http://127.0.0.1:8000/docs

## API Endpoint
POST /summarize

Request:
{
  "report_text": "Medical report text here"
}

Response:
{
  "summary": "Summarized output"
}
