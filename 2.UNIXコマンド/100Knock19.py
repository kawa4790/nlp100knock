# 19.各行の1コラム目の文字列の出現頻度を求め, 出現頻度の高い順に並べる
import pandas as pd

df = pd.read_csv('../NLP100Knock/popular-names.txt', sep='\t', header=None)
print(df[0].value_counts())
        
# cut -f 1 popular-names.txt | sort | uniq -c | sort -r -n