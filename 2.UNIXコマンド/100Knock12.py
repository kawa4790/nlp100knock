# 12.1列目をcol1.txtに, 2列目をcol2.txtに保存
import pandas as pd

df = pd.read_csv('../NLP100Knock/popular-names.txt', sep='\t', header=None)
df[0].to_csv('../NLP100Knock/col1.txt', index=False, header=None)
df[1].to_csv('../NLP100Knock/col2.txt', index=False, header=None)

# cut -f 1 '../NLP100Knock/popular-names.txt'
# cut -f 2 '../NLP100Knock/popular-names.txt'