# 70.単語埋め込みの読み込み
import numpy as np
from gensim.models import KeyedVectors

def load_pretrained_embeddings(model_path, pad_token="<pad>"):
    word_vectors = KeyedVectors.load_word2vec_format(model_path, binary=True)

    vocab_size = len(word_vectors.key_to_index) + 1  # +1 for <pad>
    embedding_dim = word_vectors.vector_size

    # 埋め込み行列と辞書の初期化
    embedding_matrix = np.zeros((vocab_size, embedding_dim), dtype=np.float32)
    word_to_id = {pad_token: 0}
    id_to_word = {0: pad_token}

    for index, word in enumerate(word_vectors.key_to_index, start=1):
        word_to_id[word] = index
        id_to_word[index] = word
        embedding_matrix[index] = word_vectors[word]

    return embedding_matrix, word_to_id, id_to_word

embedding_path = '/home/j138kawa/NLP100Knock/GoogleNews-vectors-negative300.bin.gz'
embedding_matrix, word_to_id, id_to_word = load_pretrained_embeddings(embedding_path)

print(f"Embedding matrix shape: {embedding_matrix.shape}")