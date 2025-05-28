# 77.GPU上での学習
# 77.GPU上での学習
from torch.utils.data import DataLoader
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class LogisticRegression(nn.Module):
  def __init__(self, embedding_matrix, freeze_embedding):
    super().__init__()
    self.embedding = nn.Embedding.from_pretrained(torch.tensor(embedding_matrix, dtype=torch.float32), freeze=freeze_embedding)
    self.linear = nn.Linear(embedding_matrix.shape[1], 1)

  def forward(self, x):
    x = self.embedding(x)
    x = torch.mean(x, dim=1)
    y = self.linear(x)
    return y

model = LogisticRegression(embedding_matrix, True).to(device)
criterion = nn.BCEWithLogitsLoss()
optimizer = torch.optim.AdamW(model.parameters())

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
