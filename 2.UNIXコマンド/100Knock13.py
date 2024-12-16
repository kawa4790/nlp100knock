# 13.col1.txtとcol2.txtをマージ
import pandas as pd

c1 = pd.read_csv('../NLP100Knock/col1.txt', header=None)
c2 = pd.read_csv('../NLP100Knock/col2.txt', header=None)

df = pd.concat([c1, c2], axis=1)
df.to_csv('../NLP100Knock/col1&2.txt', sep='\t', index=False, header=None)

# paste '../NLP100Knock/col1.txt' '../NLP100Knock/col2.txt'