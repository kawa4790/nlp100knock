# 07.テンプレートによる文生成
def Generate_sentence(x, y, z):
    sentence = str(x)+ "時の" + str(y)+ "は" + str(z)
    return sentence

result = Generate_sentence(12, "気温", 22.4)
print(result)