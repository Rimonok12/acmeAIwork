import os
import re

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

DOC_INDEX = [
    ("doc1.md", "Bangladesh Competition Act, 2012 — Anti-Competitive Agreements"),
    ("doc2.md", "Contract Act, 1872 — Breach & Remedies (Bangladesh)"),
    ("doc3.md", "Bangladesh Labour Act, 2006 — Termination & Notice"),
]


_BASE_STOPWORDS = {
    "the","a","an","and","or","of","in","to","for","on","with","by","as",
    "is","are","was","were","be","been","being","that","this","it","at",
    "from","but","not","no","if","into","than","then","there","their","its",
}


_LEGAL_STOPWORDS = {
    "act", "section", "clause", "article", "bangladesh", "of", "the" 
}

_STOPWORDS = _BASE_STOPWORDS.union(_LEGAL_STOPWORDS)

_token_re = re.compile(r"[A-Za-z][A-Za-z-]*[A-Za-z]")

def _tokenize(text: str):
    tokens = [t.lower() for t in _token_re.findall(text)]
    return [t for t in tokens if len(t) > 2 and t not in _STOPWORDS]

def _first_sentences(text: str, n: int = 2, fallback_chars: int = 280) -> str:
    parts = re.split(r"(?<=[\.\?\!])\s+", text.strip())
    if parts and parts[0]:
        summary = " ".join(parts[:n]).strip()
        if len(summary) < 40:
            return text[:fallback_chars].strip()
        return summary
    return text[:fallback_chars].strip()

def load_docs():
    docs = []
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
            "tokens": set(_tokenize(body + " " + title)),
        })
    return docs


def rank_search_results(query: str, docs):
    q_tokens = set(_tokenize(query))
    if not q_tokens:
        return [] 

    results = []
    for d in docs:
        matching_tokens = q_tokens.intersection(d["tokens"])
        score = len(matching_tokens)

        if score > 0:
            results.append({
                "docId": d["id"],
                "title": d["title"],
                "summary": _first_sentences(d["body"], 2, 280),
                "score": score,
                "matched_tokens": list(matching_tokens) 
            })
            
    results.sort(key=lambda r: r["score"], reverse=True)
    return results