from operations.generator import add_problem
from operations.question import askQuestion
import random
from typing import Optional
from fastapi import FastAPI, Request


app = FastAPI()

question = add_problem(1)
operators = {
    "Addition": "+",
    "Subtraction": "-",
    "Multiplication": "*",
    "Division": "/",
}


@app.get("/Random")
def read_root():
    return question.create_random_problem()


@app.get("/{arithmatic}")
def read_root(arithmatic: str):
    if arithmatic == "Operator":
        sign = "Operator"
    else:
        sign = operators.get(arithmatic)

    return question.create_arithmatic_problem(sign)
