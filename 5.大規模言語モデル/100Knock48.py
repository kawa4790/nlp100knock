# 48.LLMによる評価の頑健性
import google.generativeai as genai
import os
from dotenv import load_dotenv
import numpy as np

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

prompt = """
    以下の10個の川柳の面白さをそれぞれ10段階で評価してください。
    なお、出力は1~10の数字のみにしてください。先頭の番号は必要ありません

    1. 四月風　桜舞い散る　春の息吹

    2. 四月雨　しとしとと降る　芽吹きの音

    3. 新生活　四月始まる　希望胸に

    4. 桜咲く　四月満開　心躍る

    5. 四月晴れ　空高く青く　未来広がる

    6. 若葉萌え　四月鮮やか　生命力感じる

    7. 卒入学　四月告げる　新たな旅立ち

    8. 花見酒　四月夜空　月と語らう

    9. 四月一日　嘘も交えて　笑顔溢れる

    10. 待ち遠し　四月の訪れ　温もり感じる
    """

senryu_score = []
for i in range(10):
    response = model.generate_content(prompt)
    senryu_score.append(response)
    print(senryu_score)

print("分散：", np.var(senryu_score))