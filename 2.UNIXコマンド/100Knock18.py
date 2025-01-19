# 18.各行を3コラム目の数値の降順にソート
import pandas as pd

df = pd.read_csv('../NLP100Knock/popular-names.txt', sep='\t', header=None)
print(df.sort_values(2, ascending=False))
        
# sort -r -n -k 3 popular-names.txt