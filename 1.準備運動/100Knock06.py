# 06.集合
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