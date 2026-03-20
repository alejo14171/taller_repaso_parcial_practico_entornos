# Taller Repaso Parcial - FastAPI + Gemini Chatbot

A backend REST API built with FastAPI that integrates with Google Gemini to power an AI chat interface.

## Prerequisites

- Python 3.12+
- Google Gemini API Key ([get one here](https://aistudio.google.com/app/apikey))

## Project Structure
```
├── app/
│   ├── main.py
│   ├── routers/
│   │   └── chat.py
│   ├── services/
│   │   └── gemini_service.py
│   ├── models/
│   │   └── schemas.py
│   └── config/
│       └── settings.py
├── frontend/
│   └── index.html
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation
```bash
git clone https://github.com/tu-usuario/taller_repaso_parcial_practico_entornos.git
cd taller_repaso_parcial_practico_entornos
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the root directory:
```
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.0-flash
```

## Running the Backend
```bash
fastapi dev app/main.py
```

API will be available at `http://localhost:8000`

## API Documentation

Once running, visit `http://localhost:8000/docs` for the interactive Swagger UI.

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Health check |
| POST | /chat | Send a message to Gemini |

### POST /chat

**Request:**
```json
{ "message": "Hello!" }
```

**Response:**
```json
{ "reply": "Hi! How can I help you?" }
```

## Frontend

Open `frontend/index.html` with Live Server in VSCode or any local server.
