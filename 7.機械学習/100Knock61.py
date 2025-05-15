# 61.特徴ベクトル
import numpy as np
from collections import Counter


def make_dict_list(df, text_col_name, label_col_name):
    dict_list = []
    for text, label in zip(df[text_col_name], df[label_col_name]):
        tokens = text.split()
        feature_vec = dict(Counter(tokens))
        dict_list.append({"text": text, "label": label, "feature": feature_vec})
    return dict_list


train_list = make_dict_list(df_train, text_col_name="sentence", label_col_name="label")
dev_list = make_dict_list(df_dev, text_col_name="sentence", label_col_name="label")

print(train_list[0])
