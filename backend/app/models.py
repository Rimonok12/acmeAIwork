from pydantic import BaseModel
from typing import List

class GenerateRequest(BaseModel):
    query: str

class SearchResult(BaseModel):
    docId: str
    title: str
    summary: str
    matched: bool  

class GenerateResponse(BaseModel):
    query: str
    results: List[SearchResult]
