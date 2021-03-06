import streamlit as st
import numpy as np
import json
import pandas as pd
import random

from acquire.grabques import *

st.write(
    """
# Math Quiz App
    """
)

Qlist = build_question_set()
Qframe = build_question_frame()

nlist = []

if st.button("Evaluate"):
    submissions = pd.read_csv("submissions.csv", index_col="Unnamed: 0").reindex()
    q_set, num_right = evaluate_set(submissions)
    seed = random.randint(1, 100000)
    st.write("""
       """f"You got {num_right.loc['Addition'][0]} Additions problems correct."""" 

       """f"You got {num_right.loc['Subtraction'][0]} Subtraction problems correct.""""

       """f"You got {num_right.loc['Multiplication'][0]} Multiplication problems correct.""""

       """f"You got {num_right.loc['Division'][0]} Division problems correct.""""

       """f"You got {num_right.loc['Operator'][0]} Operatorion problems correct.""""
       """
    )
    Qlist = build_question_set(q_set, seed=seed)
    Qframe = build_question_frame(Qlist)
    nlist = []

Qframe.iloc[0][1]
answer = st.text_input("Please enter the Answer to Q1", value="")
answer == str(Qframe.iloc[0][0])
nlist.append(answer == str(Qframe.iloc[0][0]))

Qframe.iloc[1][1]
answer = st.text_input("Please enter the Answer to Q2", value="")
answer == str(Qframe.iloc[1][0])
nlist.append(answer == str(Qframe.iloc[1][0]))

Qframe.iloc[2][1]
answer = st.text_input("Please enter the Answer to Q3", value="")
answer == str(Qframe.iloc[2][0])
nlist.append(answer == str(Qframe.iloc[2][0]))

Qframe.iloc[3][1]
answer = st.text_input("Please enter the Answer to Q4", value="")
answer == str(Qframe.iloc[3][0])
nlist.append(answer == str(Qframe.iloc[3][0]))

Qframe.iloc[4][1]
answer = st.text_input("Please enter the Answer to Q5", value="")
answer == str(Qframe.iloc[4][0])
nlist.append(answer == str(Qframe.iloc[4][0]))

Qframe.iloc[5][1]
answer = st.text_input("Please enter the Answer to Q6", value="")
answer == str(Qframe.iloc[5][0])
nlist.append(answer == str(Qframe.iloc[5][0]))

Qframe.iloc[6][1]
answer = st.text_input("Please enter the Answer to Q7", value="")
answer == str(Qframe.iloc[6][0])
nlist.append(answer == str(Qframe.iloc[6][0]))

Qframe.iloc[7][1]
answer = st.text_input("Please enter the Answer to Q8", value="")
answer == str(Qframe.iloc[7][0])
nlist.append(answer == str(Qframe.iloc[7][0]))

Qframe.iloc[8][1]
answer = st.text_input("Please enter the Answer to Q9", value="")
answer == str(Qframe.iloc[8][0])
nlist.append(answer == str(Qframe.iloc[8][0]))

Qframe.iloc[9][1]
answer = st.text_input("Please enter the Answer to Q10", value="")
answer == str(Qframe.iloc[9][0])
nlist.append(answer == str(Qframe.iloc[9][0]))

Qframe["Correct"] = nlist

if st.button("Save Answers"):
    Qframe.to_csv("submissions.csv")