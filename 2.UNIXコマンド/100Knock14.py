# 14.先頭からN行を出力
with open("../NLP100Knock/popular-names.txt", "r") as f:
    N = int(input())
    lines = f.readlines()
    for i in range(N):
        lines[i] = lines[i].replace('\n', '')
        print(lines[i])
        
# head -n 5 "../NLP100Knock/popular-names.txt"