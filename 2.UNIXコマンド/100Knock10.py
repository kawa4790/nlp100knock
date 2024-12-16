# 10.行数のカウント
with open("../NLP100Knock/popular-names.txt", "r") as f:
    lines = f.readlines()
    print(len(lines))
    
# wc -l "../NLP100Knock/popular-names.txt"