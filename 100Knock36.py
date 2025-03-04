# 36.頻度上位10語
%matplotlib inline
import matplotlib.pyplot as plt
import japanize_matplotlib

word_list = []
height_list = []
for i in range(10):
    word_list.append(desc_list.most_common()[:10][i][0]) #cは前問で求める
    height_list.append(desc_list.most_common()[:10][i][1])
plt.bar(x = word_list ,height = height_list)

