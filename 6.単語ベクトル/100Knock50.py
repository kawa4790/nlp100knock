# 50.単語ベクトルの読み込みと表示
from gensim.models import KeyedVectors

file = '/home/j138kawa/NLP100Knock/GoogleNews-vectors-negative300.bin.gz'
model = KeyedVectors.load_word2vec_format(file, binary=True)
print(model['United_States'])