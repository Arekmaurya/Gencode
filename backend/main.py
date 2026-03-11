import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import ExecuteRequest, ExecuteResponse
from db import get_all_problems, get_problem_by_id
from execution_engine import run_code

app = FastAPI(title="GenCode API")

# Configure CORS
# For MVP, we'll allow all origins to ensure the frontend can always connect.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
