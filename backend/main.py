import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.models import ExecuteRequest, ExecuteResponse
from backend.db import get_all_problems, get_problem_by_id
from backend.execution_engine import run_code

app = FastAPI(title="GenCode API")

# Configure CORS
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")
ALLOWED_ORIGINS = [FRONTEND_URL, "http://localhost:3000"]
# In production, FRONTEND_URL will be provided via Render environment variables

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to GenCode API"}

@app.get("/api/health")
def health_check():
    return {"status": "ok"}

@app.get("/api/problems")
def read_problems():
    return get_all_problems()

@app.get("/api/problems/{problem_id}")
def read_problem(problem_id: str):
    p = get_problem_by_id(problem_id)
    if not p:
        raise HTTPException(status_code=404, detail="Problem not found")
    return p

@app.post("/api/execute", response_model=ExecuteResponse)
def execute_code(req: ExecuteRequest):
    p = get_problem_by_id(req.problem_id)
    if not p:
        raise HTTPException(status_code=404, detail="Problem not found")
        
    return run_code(code=req.code, problem_id=req.problem_id)
