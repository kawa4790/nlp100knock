# 34.名詞の連接
cnct_noun_list = []
for sentense in sentences_list:
    count = 0
    noun = ""
    for i in range(len(sentense)):
        if sentense[i]["pos"] == "名詞":
            count += 1
            noun += sentense[i]["surface"]
        else:
            if count > 1:
              cnct_noun_list.append(noun)
            count = 0
            noun = ""
noun_set = set(cnct_noun_list)
print(noun_set)