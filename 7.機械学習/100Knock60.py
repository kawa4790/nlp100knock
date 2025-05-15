# 60.データの入手・整形
import pandas as pd

df_train = pd.read_csv("SST-2/train.tsv", sep="\t")
df_dev = pd.read_csv("SST-2/dev.tsv", sep="\t")

print(f"train\tpositive：{(df_train['label']==1).sum()}, negative：{(df_train['label']==0).sum()}")
print(f"dev\tpositive：{(df_dev['label']==1).sum():5d}, negative：{(df_dev['label']==0).sum():5d}")
