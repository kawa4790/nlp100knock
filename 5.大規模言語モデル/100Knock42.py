# 42.多肢選択問題の正解率
from dotenv import load_dotenv
import google.generativeai as genai
import os
import time
import pandas as pd
from sklearn.metrics import accuracy_score

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

df = pd.read_csv("JMMLU/JMMLU/astronomy.csv", header=None)
df.columns = ["問題", "A", "B", "C", "D", "正解"]

questions = df["問題"]
choice1 = df["A"]
choice2 = df["B"]
choice3 = df["C"]
choice4 = df["D"]
correct_answers = df["正解"]
pred_answers = []

model = genai.GenerativeModel("gemini-1.5-flash")

count = 0
for question, A, B, C, D in zip(questions, choice1, choice2, choice3, choice4):

    prompt = (
        "以下の問題について正しい選択しを選んでください。\n"
        "解答は必ずA,B,C,Dのいずれか一文字のみにしてください。\n\n"
        f"問題：{question}\n"
        f"A：{A}\n"
        f"B：{B}\n"
        f"C：{C}\n"
        f"D：{D}\n"
    )

    answer = ""

    response = model.generate_content(contents=prompt)
    
    count += 1
    if (count % 15 == 0):
        count = 0
        time.sleep(61)
        
    answer = response.text.replace("\n", "")

    pred_answers.append(answer)
    print(answer, end=" ")

score = accuracy_score(correct_answers, pred_answers)

print(f"\n正解率：{score:.3f}")