# 39.Zipfの法則
import matplotlib.pyplot as plt
import japanize_matplotlib
word_list = []
for sentense in sentences_list:
    for text in sentense:
        word_list.append(text["surface"])
data = collections.Counter(word_list)
temp2 = sorted((data.values()), reverse = True)
plt.plot(temp2)
plt.xlabel('出現頻度順位')
plt.ylabel('出現頻度')
ax = plt.gca()
ax.set_yscale('log')
ax.set_xscale('log')
plt.show()