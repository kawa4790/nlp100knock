# 22.カテゴリ名の抽出
import pandas as pd

df = pd.read_json('../NLP100Knock/jawiki-country.json', lines=True)
uk_text = df.query('title=="イギリス"')['text'].values[0]
uk_texts = uk_text.split('\n')
ans = list(filter(lambda x: '[Category:' in x, uk_texts))
ans = [a.replace('[[Category:', '').replace('|*', '').replace(']]', '') for a in ans]
print(ans)