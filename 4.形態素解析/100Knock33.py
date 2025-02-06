# 33.「AのB」
np_list = []
for sentense in sentences_list:
    for i in range(len(sentense)):
        if sentense[i-1]["pos"]=="名詞" and sentense[i]["surface"] == "の" and sentense[i+1]["pos"]=="名詞":
            np_list.append(sentense[i - 1]["surface"] + "の" + sentense[i + 1]["surface"])
print(np_list)