# 15.末尾のN行を出力
with open("../NLP100Knock/popular-names.txt", "r") as f:
    N = int(input())
    lines = f.readlines()
    for i in range(len(lines)-N, len(lines)):
        lines[i] = lines[i].replace('\n', '')
        print(lines[i])
        
# tail -n 5 popular-names.txt