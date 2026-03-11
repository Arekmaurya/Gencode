from typing import List
from pydantic import BaseModel

class Problem(BaseModel):
    id: str
    title: str
    difficulty: str
    description: str
    starting_code: str

# Mock database
PROBLEMS = [
    Problem(
        id="1",
        title="1. Implement Linear Regression Prediction",
        difficulty="Easy",
        description="Write a function `predict(x, w, b)` that computes the linear regression prediction $y = wx + b$.",
        starting_code="def predict(x, w, b):\n    # Your code here\n    pass\n"
    ),
    Problem(
        id="2",
        title="2. Softmax Function",
        difficulty="Medium",
        description="Implement the softmax function `softmax(z)` which normalizes an array of values to a probability distribution.",
        starting_code="import numpy as np\n\ndef softmax(z):\n    # Your code here\n    pass\n"
    )
]

def get_all_problems() -> List[Problem]:
    return PROBLEMS

def get_problem_by_id(problem_id: str) -> Problem | None:
    for p in PROBLEMS:
        if p.id == problem_id:
            return p
    return None
