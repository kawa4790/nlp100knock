# 35.単語の出現頻度
import collections
word_list = []
for sentense in sentences_list:
    for i in range(len(sentense)):
        if sentense[i]["pos"] != "補助記号":
            word_list.append(sentense[i]["surface"])
desc_list = collections.Counter(word_list)
print(desc_list.most_common())