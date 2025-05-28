# 79.アーキテクチャの変更
# 79.アーキテクチャの変更
from torch.utils.data import DataLoader
import torch
import torch.nn as nn
import torch.nn.functional as F

batch_size = 32
num_epochs = 5
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class CNNClassifier(nn.Module):
    def __init__(self, embedding_matrix, freeze_embedding=True, num_filters=100, kernel_sizes=[3, 4, 5]):
        super().__init__()
        vocab_size, embedding_dim = embedding_matrix.shape

        self.embedding = nn.Embedding.from_pretrained(
            torch.tensor(embedding_matrix, dtype=torch.float32),
            freeze=freeze_embedding
        )

        self.convs = nn.ModuleList([
            nn.Conv1d(in_channels=embedding_dim, out_channels=num_filters, kernel_size=k)
            for k in kernel_sizes
        ])

        self.fc = nn.Linear(num_filters * len(kernel_sizes), 1)

    def forward(self, input_ids):
        embedded = self.embedding(input_ids)  # shape: (batch_size, seq_len, embedding_dim)
        embedded = embedded.transpose(1, 2)   # shape: (batch_size, embedding_dim, seq_len)

        conv_outputs = [F.relu(conv(embedded)) for conv in self.convs]  # list of (batch_size, num_filters, *)
        pooled_outputs = [F.max_pool1d(output, kernel_size=output.size(2)).squeeze(2) for output in conv_outputs]
        concat = torch.cat(pooled_outputs, dim=1)  # shape: (batch_size, num_filters * len(kernel_sizes))

        logits = self.fc(concat)
        return logits

train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True, collate_fn=collate)
dev_loader = DataLoader(dev_data, batch_size=batch_size, shuffle=False, collate_fn=collate)

model = CNNClassifier(embedding_matrix, True).to(device)
criterion = nn.BCEWithLogitsLoss()
optimizer = torch.optim.AdamW(model.parameters())

def compute_accuracy(y_true, y_pred):
    y_true = np.array(y_true).astype(int)
    y_pred = (np.array(y_pred) >= 0.5).astype(int)
    return (y_true == y_pred).mean()

# 学習
for epoch in range(num_epochs):
  model.train()
  train_loss = []
  for batch in train_loader:
    x = batch['input_ids'].to(device)
    y = batch['label'].to(device)
    optimizer.zero_grad()
    y_pred = model(x)
    loss = criterion(y_pred, y)
    loss.backward()
    optimizer.step()
    train_loss.append(loss.item())

  model.eval()
  dev_loss, y_pred_list, y_list = [], [], []
  with torch.no_grad():
    for batch in dev_loader:
      x = batch['input_ids'].to(device)
      y = batch['label'].to(device)
      y_pred = model(x)
      loss = criterion(y_pred, y)
      dev_loss.append(loss.item())
      y_list.extend(y.cpu().numpy())
      y_pred_list.extend((y_pred > 0.5).float().cpu().numpy())
    
  print(f'[epoch {epoch + 1}/{num_epochs}] train loss: {np.mean(train_loss):.4f}, dev loss: {np.mean(dev_loss):.4f}, acc: {compute_accuracy(y_list, y_pred_list):.4f}')


