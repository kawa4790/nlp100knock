# 52.類似度の高い単語10件
similarity_top10 = model.most_similar('United_States', topn=10)
for word in similarity_top10:
    print(f"{word[0]}, 類似度:{word[1]}")