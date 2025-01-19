# 17.1列目の文字列の異なり
import pandas as pd

df = pd.read_csv('../NLP100Knock/popular-names.txt', sep='\t', header=None)
txt =  df[0].unique()
txt.sort()
print(txt)
        
# cut -f 1 popular-names.txt | sort | uniq