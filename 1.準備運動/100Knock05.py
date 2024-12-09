# 05.n-gram
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

w, c = N_gram(2, "I am an NLPer")
print("単語bi-gram",w)
print("文字bi-gram",c)