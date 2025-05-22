# 72.Bag of wordsモデルの構築
import torch
import torch.nn as nn

class MeanEmbeddingClassifier(nn.Module):
    def __init__(self, embedding_matrix):
        super().__init__()
        embedding_tensor = torch.tensor(embedding_matrix, dtype=torch.float32)
        embedding_dim = embedding_tensor.shape[1]

        self.embedding_layer = nn.Embedding.from_pretrained(embedding_tensor, freeze=True)
        self.classifier = nn.Linear(embedding_dim, 1)

    def forward(self, token_ids):
        embedded_tokens = self.embedding_layer(token_ids)        
        sentence_embeddings = embedded_tokens.mean(dim=1)         
        logits = self.classifier(sentence_embeddings)             
        return logits
