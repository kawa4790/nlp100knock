# 78.単語埋め込みのファインチューニング

import torch
import torch.nn as nn
import numpy as np
from torch.utils.data import DataLoader
from tqdm import tqdm

batch_size = 32
num_epochs = 5
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class LogisticRegression(nn.Module):
    def __init__(self, embedding_matrix):
        super().__init__()
        self.embedding = nn.Embedding.from_pretrained(
            torch.tensor(embedding_matrix, dtype=torch.float32),
            freeze=False  # ファインチューニングを有効にする
        )
        self.linear = nn.Linear(embedding_matrix.shape[1], 1)

    def forward(self, x):
        x = self.embedding(x)
        x = torch.mean(x, dim=1)
        return self.linear(x)

train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True, collate_fn=collate)
dev_loader = DataLoader(dev_data, batch_size=batch_size, shuffle=False, collate_fn=collate)

model = LogisticRegression(embedding_matrix).to(device)
criterion = nn.BCEWithLogitsLoss()
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4)



# 学習ループ
for epoch in range(num_epochs):
    model.train()
    train_loss = []
    for batch in tqdm(train_loader, desc=f"Epoch {epoch+1} - Training"):
        x = batch['input_ids'].to(device)
        y = batch['label'].to(device)
        optimizer.zero_grad()
        y_pred = model(x)
        loss = criterion(y_pred, y)
        loss.backward()
        optimizer.step()
        train_loss.append(loss.item())

    model.eval()
    dev_loss, y_true_list, y_pred_list = [], [], []
    with torch.no_grad():
        for batch in dev_loader:
            x = batch['input_ids'].to(device)
            y = batch['label'].to(device)
            y_pred = model(x)
            loss = criterion(y_pred, y)
            dev_loss.append(loss.item())
            y_true_list.extend(y.cpu().numpy())
            y_pred_list.extend(torch.sigmoid(y_pred).cpu().numpy())

    acc = compute_accuracy(y_true_list, y_pred_list)
    print(f"[Epoch {epoch+1}] Train Loss: {np.mean(train_loss):.4f}, Dev Loss: {np.mean(dev_loss):.4f}, Accuracy: {acc:.4f}")
