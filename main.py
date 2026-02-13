from fastapi import FastAPI
from app.routes.summarize import router as summarize_router

app = FastAPI(
    title="AI Medical Report Summarizer",
    version="1.0.0"
)

app.include_router(summarize_router)

@app.get("/")
def home():
    return {"message": "Medical Report Summarizer API is running"}
