#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
pip install "fastapi==0.95.2" "pydantic==1.10.13" "uvicorn==0.22.0" "starlette==0.27.0" "anyio==3.7.1"
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
