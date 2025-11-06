# ⚖️ Acme Work Portal

A full-stack web application built with **React + Vite** (frontend) and **FastAPI** (backend).  
It provides a simple legal text search experience — fast, lightweight, and easy to deploy.

---

## 🚀 Features
- 🔍 Keyword-based legal document search (no external API calls)
- ⚡ Frontend built with **React + Vite**
- 🐍 Backend powered by **FastAPI**
- 🔄 Live reload for local development
- 🌍 CORS enabled (ready for frontend integration)
- 🧩 Supports multiple backend ports dynamically
- 🐳 Easy Docker setup for deployment

---

## 📁 Project Structure

acmeAIwork/
│
├── frontend/ # React + Vite frontend
│ ├── src/
│ ├── public/
│ ├── package.json
│ ├── vite.config.js
│ └── .env # backend API URL(s)
│
├── backend/ # FastAPI backend
│ ├── app/
│ │ ├── init.py
│ │ ├── main.py # FastAPI entrypoint
│ │ ├── logic.py # document search logic
│ │ ├── models.py # Pydantic models
│ │ └── data/
│ │ ├── doc1.md
│ │ ├── doc2.md
│ │ └── doc3.md
│ ├── requirements.txt
│ └── Dockerfile
│
└── README.md



## ⚙️ Backend Setup (FastAPI)

1️⃣ Create and activate a virtual environment:

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate

2️⃣ Install dependencies:

pip install -r requirements.txt

3️⃣ Run the API server:
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000


**💻 Frontend Setup (React + Vite)**
1️⃣ Move to the frontend folder
cd frontend

2️⃣ Install dependencies
npm install

3️⃣ Configure backend API URL(s)

In .env (create if missing):

Single backend
VITE_API_BASE=http://localhost:8000

Multiple backends (auto-fallback)
VITE_API_BASES=http://localhost:8001;http://localhost:8000;http://localhost:8002

4️⃣ Run the frontend
npm run dev



