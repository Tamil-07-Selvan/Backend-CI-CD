from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to access this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend URL in production
    allow_methods=["*"],
    allow_headers=["*"],
)

class RequestModel(BaseModel):
    array: List[int]
    windowSize: int

@app.post("/max-sum")
def max_sum(data: RequestModel):
    arr = data.array
    k = data.windowSize
    if len(arr) < k:
        return {"result": -1}

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return {"result": max_sum}
