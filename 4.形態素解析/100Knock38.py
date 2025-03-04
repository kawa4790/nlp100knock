# 38.ヒストグラム
import matplotlib.pyplot as plt
word_list = []
for sentense in sentences_list:
    for text in sentense:
        word_list.append(text["surface"])
data = collections.Counter(word_list)
plt.hist(data.values(), range(1, 15))
