# 37.「猫」と共起頻度の高い上位10語
import itertools
import matplotlib.pyplot as plt
import japanize_matplotlib
%matplotlib inline

neko_list = []
for sentense in sentences_list:
    text37 = []
    Flag = 0
    for text in sentense:
        if "猫" in text["surface"]:
            Flag = 1
            continue
        if text["pos"] != "補助記号" and text["pos"] != "助詞" and text["pos"] != "助動詞":
            text37.append(text["surface"])
    if Flag == 1:
        neko_list.append(text37)
all_neko = list(itertools.chain.from_iterable(neko_list))
c = collections.Counter(all_neko)
word_list = []
height_list = []
for i in range(10):
    word_list.append(c.most_common()[:10][i][0])
    height_list.append(c.most_common()[:10][i][1])
plt.bar(x = word_list, height = height_list)