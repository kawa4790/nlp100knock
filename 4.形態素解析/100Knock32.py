# 32.動詞の基本形
base_verb_list = []
for sentense in sentences_list:
    for text in sentense:
        if text["pos"] == "動詞":
            base_verb_list.append(text["base"])
base_verb = set(base_verb_list)
print(base_verb)