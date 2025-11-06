# backend/app/logic.py

import os
import re
from typing import List, Dict, Any

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

DOC_INDEX = [
    ("doc1.md", "Bangladesh Competition Act, 2012 — Anti-Competitive Agreements"),
    ("doc2.md", "Contract Act, 1872 — Breach & Remedies (Bangladesh)"),
    ("doc3.md", "Bangladesh Labour Act, 2006 — Termination & Notice"),
]

# Basic stopwords only (as in your version)
_STOPWORDS = {
    "the","a","an","and","or","of","in","to","for","on","with","by","as",
    "is","are","was","were","be","been","being","that","this","it","at",
    "from","but","not","no","if","into","than","then","there","their","its",
}

# Simple alpha word tokenizer
_token_re = re.compile(r"[A-Za-z]+")

def _tokenize(text: str) -> List[str]:
    tokens = [t.lower() for t in _token_re.findall(text or "")]
    return [t for t in tokens if t not in _STOPWORDS]

def _first_sentences(text: str, n: int = 2, fallback_chars: int = 280) -> str:
    parts = re.split(r"(?<=[\.\?\!])\s+", (text or "").strip())
    if parts and parts[0]:
        summary = " ".join(parts[:n]).strip()
        if len(summary) < 40:
            return (text or "")[:fallback_chars].strip()
        return summary
    return (text or "")[:fallback_chars].strip()

def load_docs() -> List[Dict[str, Any]]:
    docs: List[Dict[str, Any]] = []
    for fname, title in DOC_INDEX:
        path = os.path.join(DATA_DIR, fname)
        body = ""
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                body = f.read()
        docs.append({
            "id": os.path.splitext(fname)[0],
            "title": title,
            "body": body,
            "tokens": set(_tokenize(f"{body} {title}")),
        })
    return docs

def search_and_flag(query: str, docs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Boolean match: mark a doc as matched if ANY query token appears in its token set.
    Returns matched docs first (alphabetical by title), then unmatched.
    """
    q_tokens = list(set(_tokenize(query)))
    if not q_tokens:
        # If query becomes empty (after stopword filtering), nothing matches.
        return [{
            "docId": d["id"],
            "title": d["title"],
            "summary": _first_sentences(d["body"], 2, 280),
            "matched": False
        } for d in docs]

    results: List[Dict[str, Any]] = []
    for d in docs:
        matched = any(t in d["tokens"] for t in q_tokens)
        results.append({
            "docId": d["id"],
            "title": d["title"],
            "summary": _first_sentences(d["body"], 2, 280),
            "matched": bool(matched),
        })

    # Sort: matched first, then by title
    results.sort(key=lambda r: (not r["matched"], r["title"]))
    return results
