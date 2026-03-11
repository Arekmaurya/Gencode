from pydantic import BaseModel

class ExecuteRequest(BaseModel):
    code: str
    problem_id: str

class ExecuteResponse(BaseModel):
    status: str # "pass", "fail", "error"
    output: str
    execution_time_ms: float
