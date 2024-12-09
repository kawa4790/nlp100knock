# 06.集合
def N_gram(n, text):
    word = text.split(" ")
    char = text.replace(" ", "")
    word_list = []
    char_list = []
    
    for i in range(len(word)):
        word_list.append(word[i:n+i])
    for i in range(len(char)):
        char_list.append(char[i:n+i])
    return word_list, char_list

a = "paraparaparadise"
b = "paragraph"
_, a_bi = N_gram(2, a)
_, b_bi = N_gram(2, b)
X = set(a_bi)
Y = set(b_bi)
print("和集合:", X | Y)
print("積集合:", X & Y)
print("差集合:", X - Y)

serch_bi = "se"
if serch_bi in X:
  print("Xに{}が含まれる".format(serch_bi))
elif serch_bi in Y:
  print("Yに{}が含まれる".format(serch_bi))
else:
  print("XとYに{}は含まれない".format(serch_bi))