from transformers import pipeline
import os
from dotenv import load_dotenv

load_dotenv()
MODEL_NAME = os.getenv("MODEL_NAME", "sshleifer/distilbart-cnn-12-6")

summarizer = pipeline("summarization", model=MODEL_NAME)

def generate_summary(text: str) -> str:
    """Generate a summary for the given text using a pre-trained model."""
    result = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return result[0]['summary_text']
# Example usage