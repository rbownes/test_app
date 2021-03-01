import requests
import pandas as pd
import numpy as np
import streamlit as st
import random
import os
import json

def grabQuestions(list_of_questions: list):
    """
    """
    use_case = list_of_questions[0]
    num_ques = list_of_questions[1]
    questions = []
    question_set = {"Answer": [], 
                    "Question": [], 
                    "Type": [], 
                    "Correct": [0 for i in range(num_ques)]}

    for i in range(num_ques):
        responses = requests.get(f"http://127.0.0.1:8000/{use_case}").json()

        question_set["Answer"].append(responses[0])
        question_set["Question"].append(responses[1])
        question_set["Type"].append(responses[2])

    return question_set

@st.cache
def build_question_set(num_dict = {'Addition': 2, 
                                   'Subtraction': 2, 
                                   'Multiplication': 2, 
                                   'Division': 2, 
                                   'Operator': 2}, seed = 42):
    Qlist = [
             ["Addition", num_dict.get("Addition")], 
             ["Subtraction", num_dict.get("Subtraction")], 
             ["Multiplication", num_dict.get("Multiplication")], 
             ["Division", num_dict.get("Division")], 
             ["Operator", num_dict.get("Operator")]
             ]

    Qlist = [i for i in Qlist if i[1] !=0]
    
    nlist = []
    for i in Qlist:
        qs = grabQuestions(i)
        nlist.append(qs)
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(nlist, f, ensure_ascii=False, indent=4)

    return nlist

def build_question_frame(qlist=[{'Answer': [15, 14], 'Question': ['10 + 5 = __', '9 + 5 = __'], 'Type': ['Addition', 'Addition'], 'Correct': [0, 0]}, {'Answer': [5, 7], 'Question': ['10 - 5 = __', '10 - 3 = __'], 'Type': ['Subtraction', 'Subtraction'], 'Correct': [0, 0]}, {'Answer': [7, 40], 'Question': ['7 * 1 = __', '10 * 4 = __'], 'Type': ['Multiplication', 'Multiplication'], 'Correct': [0, 0]}, {'Answer': [3.0, 4.0], 'Question': ['6 / 2 = __', '8 / 2 = __'], 'Type': ['Division', 'Division'], 'Correct': [0, 0]}, {'Answer': ['-', '*'], 'Question': ['8 __ 1 = 7', '10 __ 5 = 50'], 'Type': ['Operator', 'Operator'], 'Correct': [0, 0]}]):
    cols = ["Answer", "Question", "Type", "Correct"]
    df = pd.DataFrame()
    initial_scores = [0,0,0,0,0,0,0,0,0,0]

    if os.path.isfile("data.json"):
        rd = pd.read_json("data.json")
        dlist = []
        for i in cols:
            dcol = rd[i].explode()
            dlist.append(dcol)
        
        for i in range(len(dlist)):
            df[i] = dlist[i]

        df.columns = cols

        df["Correct"] = initial_scores

        return df

    else:
        nlist = []
        mlist = []
        for i in cols:
            nlist = []
            for j in qlist:
                nlist += j[i]
            mlist.append(nlist)
        
        for i in range(len(mlist)):
            df[i] = mlist[i]
        
        df.columns = cols

        df["Correct"] = initial_scores

        return df


def evaluate_set(dfa):
    ords = list(dfa.groupby(["Type"]).mean().sort_values("Correct").index)
    
    return {ords[0]: 3, ords[1]: 3, ords[2]: 2, ords[3]: 1, ords[4]: 1}