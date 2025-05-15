# summarize-12facto


This FastAPI project provides an API to summarize long documents using a pre-trained Hugging Face model (`distilbart-cnn-12-6`).

## 🚀 Features
- Summarizes long text documents.
- Easy-to-use REST API.
- CI/CD pipeline with GitHub Actions.
- Dockerized for deployment.

## 📦 Requirements
- Python 3.10+

## 📁 Installation
```bash
git clone https://github.com/yourusername/document-summary-api.git
cd document-summary-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 🔧 Environment Setup
Create a `.env` file:
```env
MODEL_NAME=sshleifer/distilbart-cnn-12-6
```

## ▶️ Run the API
```bash
uvicorn app.main:app --reload
```

- Swagger UI: http://localhost:8000/docs
- Redoc UI: http://localhost:8000/redoc

## 📦 Docker
```bash
docker build -t document-summary-api .
docker run -p 8000:8000 document-summary-api
```

## ✅ Testing
```bash
pytest
```

## 🧪 CI/CD
This project includes a GitHub Actions workflow that:
- Installs dependencies
- Lints code with flake8
- Verifies summarizer pipeline
- Builds Docker image

## 📫 API Endpoints
- `GET /` – Welcome message
- `POST /summarize` – Provide JSON with `text` field and receive summary

```json
{
  "text": "Your long input text here..."
}
```


<!-- Triggering pull request CI -->


## 📄 License
MIT License
