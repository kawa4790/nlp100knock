# 53.加法構成性によるアナロジー
similarity_top10 = model.most_similar(positive=['Spain', 'Athens'], negative=['Madrid'], topn=10)
for word in similarity_top10:
    print(f"{word[0]}, 類似度:{word[1]}")