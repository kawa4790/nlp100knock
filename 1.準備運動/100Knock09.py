# 09.Typoglycemia
import random
s = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
s = s.replace(".", "")
s_list = s.split(" ")
temp = ""
for txt in s_list:
    if len(txt) <= 4:
        pass
    else:
        txt = txt[0]+"".join(random.sample(txt[1:-1], len(txt[1:-1])))+txt[-1]
    temp += txt + " "
result = temp[:-1] + "."
print(result)