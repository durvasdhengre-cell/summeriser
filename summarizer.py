from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from app.core.config import settings

class MedicalSummarizer:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("t5-small")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("t5-small")


    def summarize(self, text: str) -> str:
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            max_length=1024
        )

        summary_ids = self.model.generate(
            inputs["input_ids"],
            max_length=200,
            min_length=50,
            num_beams=4,
            length_penalty=2.0,
            early_stopping=True
        )

        summary = self.tokenizer.decode(
            summary_ids[0],
            skip_special_tokens=True
        )

        return summary


# Load model once at startup
summarizer_instance = MedicalSummarizer()
