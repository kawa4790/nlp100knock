# 31.動詞
verb_list = []
for sentense in sentences_list:
    for text in sentense:
        if text["pos"] == "動詞":
            verb_list.append(text["surface"])
verb = set(verb_list)
print(verb)