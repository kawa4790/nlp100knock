# 24.ファイル参照の抽出
import re
import pandas as pd

df = pd.read_json('../NLP100Knock/jawiki-country.json', lines=True)
uk_text = df.query('title=="イギリス"')['text'].values[0]
for file in re.findall(r'\[\[(ファイル|File):([^]|]+?)(\|.*?)+\]\]', uk_text):
    print(file[1])