from pydantic import BaseModel, Field

class MedicalReportRequest(BaseModel):
    report_text: str = Field(..., example="Patient is a 50-year-old male with diabetes...")

class MedicalReportResponse(BaseModel):
    summary: str
