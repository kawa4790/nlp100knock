# 26.強調マークアップの除去
import re
import pandas as pd


def remove_stress(dc):
    r = re.compile("'+")
    return {k: r.sub('', v) for k, v in dc.items()}


df = pd.read_json('../NLP100Knock/jawiki-country.json', lines=True)
uk_text = df.query('title=="イギリス"')['text'].values[0]
uk_texts = uk_text.split('\n')

pattern = re.compile('\|(.+?)\s=\s*(.+)')
ans = {}
for line in uk_texts:
    r = re.search(pattern, line)
    if r:
        ans[r[1]] = r[2]
print(remove_stress(ans))