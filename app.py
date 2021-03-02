import streamlit as st
import numpy as np
import json
import pandas as pd
import random

from acquire.grabques import *

from operations.question import askQuestion
import random
from typing import Optional
from fastapi import FastAPI, Request


app = FastAPI()

question = add_problem(1)
operators = {"Addition":"+",
             "Subtraction":"-", 
             "Multiplication":"*", 
             "Division":"/"}

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

import uvicorn

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, log_level="info")


st.write("""
# My First App
""")

Qlist = build_question_set()
Qframe = build_question_frame()

nlist = []

if st.button("Evaluate"):
    q_set = evaluate_set(Qframe)
    seed = random.randint(1,100000)
    Qlist = build_question_set(q_set, seed=seed)
    Qframe = build_question_frame(Qlist)
    nlist = []

Qframe.iloc[0][1]
answer = st.text_input("Please enter the Answer to Q1", value = "")
answer == str(Qframe.iloc[0][0])
nlist.append(answer == str(Qframe.iloc[0][0]))

Qframe.iloc[1][1]
answer = st.text_input("Please enter the Answer to Q2", value = "")
answer == str(Qframe.iloc[1][0])
nlist.append(answer == str(Qframe.iloc[1][0]))

Qframe.iloc[2][1]
answer = st.text_input("Please enter the Answer to Q3", value = "")
answer == str(Qframe.iloc[2][0])
nlist.append(answer == str(Qframe.iloc[2][0]))

Qframe.iloc[3][1]
answer = st.text_input("Please enter the Answer to Q4", value = "")
answer == str(Qframe.iloc[3][0])
nlist.append(answer == str(Qframe.iloc[3][0]))

Qframe.iloc[4][1]
answer = st.text_input("Please enter the Answer to Q5", value = "")
answer == str(Qframe.iloc[4][0])
nlist.append(answer == str(Qframe.iloc[4][0]))

Qframe.iloc[5][1]
answer = st.text_input("Please enter the Answer to Q6", value = "")
answer == str(Qframe.iloc[5][0])
nlist.append(answer == str(Qframe.iloc[5][0]))

Qframe.iloc[6][1]
answer = st.text_input("Please enter the Answer to Q7", value = "")
answer == str(Qframe.iloc[6][0])
nlist.append(answer == str(Qframe.iloc[6][0]))

Qframe.iloc[7][1]
answer = st.text_input("Please enter the Answer to Q8", value = "")
answer == str(Qframe.iloc[7][0])
nlist.append(answer == str(Qframe.iloc[7][0]))

Qframe.iloc[8][1]
answer = st.text_input("Please enter the Answer to Q9", value = "")
answer == str(Qframe.iloc[8][0])
nlist.append(answer == str(Qframe.iloc[8][0]))

Qframe.iloc[9][1]
answer = st.text_input("Please enter the Answer to Q10", value = "")
answer == str(Qframe.iloc[9][0])
nlist.append(answer == str(Qframe.iloc[9][0]))

Qframe["Correct"] = nlist

Qframe