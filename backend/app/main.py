from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .models import GenerateRequest, GenerateResponse, SearchResult
from .logic import load_docs, search_and_flag  # <-- changed

app = FastAPI(title="Legal Search Mock API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DOCS = load_docs()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate", response_model=GenerateResponse)
def generate(body: GenerateRequest):
    q = (body.query or "").strip()
    if not q:
        raise HTTPException(status_code=400, detail="Query must not be empty.")
    results_raw = search_and_flag(q, DOCS)  # <-- changed
    results = [SearchResult(**r) for r in results_raw]
    return GenerateResponse(query=q, results=results)
