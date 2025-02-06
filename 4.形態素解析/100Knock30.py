# 30.形態素解析結果の読み込み
with open("/home/kawano/NLP100Knock/tmp/neko.txt.mecab", "r") as f:
  lines = f.readlines()    
  sentences_list = []
  word_list = []
  
  for text in lines:
    word_dic = {}
    morpheme = text.split("\t")
    if morpheme[0] == "EOS\n":
      continue
    temp = morpheme[1].split(',')
    word_dic["surface"] = morpheme[0]
    if len(temp) <= 7:
      word_dic["base"] = morpheme[0]
    else:
      word_dic["base"] = temp[7]
    word_dic["pos"] = temp[0]
    word_dic["pos1"] = temp[1]
    word_list.append(word_dic)
    if morpheme[0]=="。":
      sentences_list.append(word_list)
      word_list = []
sentences_list