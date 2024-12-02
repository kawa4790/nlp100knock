# 03.円周率
s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
s = s.replace('.', '').replace(',', '')
s_list = [len(w) for w in s.split()]
print(s_list)