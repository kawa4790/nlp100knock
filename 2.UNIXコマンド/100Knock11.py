# 11.タブをスペースに置換
with open("../NLP100Knock/popular-names.txt", "r") as f:
    for line in f:
        print(line.replace('\t', ' '))
        
# cat "../NLP100Knock/popular-names.txt" | sed 's/\t/ /g'