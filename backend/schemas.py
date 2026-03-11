from pydantic import BaseModel, EmailStr
from typing import List, Optional

class ExecuteRequest(BaseModel):
    code: str
    problem_id: str

class ExecuteResponse(BaseModel):
    status: str # "pass", "fail", "error"
    output: str
    execution_time_ms: float

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

class ProblemBase(BaseModel):
    title: str
    difficulty: str
    description: str
    starting_code: str

class ProblemCreate(ProblemBase):
    pass

class Problem(ProblemBase):
    id: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
