# 54.アナロジーデータでの実験
results = []
file = "questions-words.txt"
with open(file, "r", encoding="utf-8") as f:
    in_section = False
    for line in f:
        line = line.strip()
        if line.startswith(":"):
            in_section = (line.lower() == ": capital-common-countries")
            continue
        if not in_section or line == "":
            continue

        a, b, c, actual = line.split()
        # アナロジー: vec(b) - vec(a) + vec(c)
        result = model.most_similar(positive=[b, c], negative=[a], topn=1)
        predicted, similarity = result[0]
        results.append((a, b, c, actual, predicted, similarity))

for r in results[:10]: 
    print(f"{r[0]} {r[1]} {r[2]} {r[3]} -> {r[4]} 類似度:{r[5]}")