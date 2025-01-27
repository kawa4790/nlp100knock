# 21.カテゴリ名を含む行を抽出
import pandas as pd

df = pd.read_json('../NLP100Knock/jawiki-country.json', lines=True)
uk_text = df.query('title=="イギリス"')['text'].values[0]
uk_texts = uk_text.split('\n')
ans = list(filter(lambda x: '[Category:' in x, uk_texts))
print(ans)