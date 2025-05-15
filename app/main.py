from fastapi import FastAPI
from pydantic import BaseModel
import logging
from app.summarize import generate_summary


# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI
app = FastAPI(
    title="Document Summary Generator API",
    description="""
    An API that uses a Hugging Face model to summarize large text content.

    ## Endpoints:
    - `GET /` → Welcome message
    - `POST /summarize` → Accepts text input and returns its summary
    """,
    version="1.0.0",
)


class TextInput(BaseModel):
    text: str


@app.get("/")
def read_root():
    """Returns a welcome message."""
    return {"message": "Welcome to the Document Summary Generator API"}


@app.post("/summarize")
def summarize_text(input: TextInput):
    """Summarizes the provided text input."""
    logger.info("Text received for summarization")
    summary = generate_summary(input.text)
    print(summary)
    return {"summary": summary}


@app.on_event("shutdown")
def shutdown_event():
    """Handles shutdown process."""
    logger.info("Shutting down application")
