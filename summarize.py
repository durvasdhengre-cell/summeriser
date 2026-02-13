from fastapi import APIRouter
from app.schemas.request_response import (
    MedicalReportRequest,
    MedicalReportResponse
)
from app.services.summarizer import summarizer_instance
from app.utils.text_cleaner import clean_text

router = APIRouter(
    prefix="/summarize",
    tags=["Summarization"]
)

@router.post("/", response_model=MedicalReportResponse)
def summarize_report(request: MedicalReportRequest):
    
    # Optional cleaning
    cleaned_text = clean_text(request.report_text)
    
    # Generate summary
    summary = summarizer_instance.summarize(cleaned_text)
    
    return MedicalReportResponse(summary=summary)
