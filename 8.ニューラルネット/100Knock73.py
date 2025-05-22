# 73.モデルの学習
import torch
import torch.nn as nn
import numpy as np
from tqdm import tqdm

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = MeanEmbeddingClassifier(embedding_matrix).to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-5)
criterion = nn.BCEWithLogitsLoss()

def train(model, train_data):
    model.train()
    total_loss = 0

    for example in tqdm(train_data, desc="Training"):
        input_ids = example["input_ids"].unsqueeze(0).to(device)  
        label = example["label"].unsqueeze(0).to(device)           

        optimizer.zero_grad()
        logits = model(input_ids)                                  
        loss = criterion(logits.squeeze(), label.squeeze())        
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    avg_loss = total_loss / len(train_data)
    return avg_loss

def evaluate(model, dev_data):
    model.eval()
    total_loss = 0

    with torch.no_grad():
        for example in dev_data:
            input_ids = example["input_ids"].unsqueeze(0).to(device)
            label = example["label"].unsqueeze(0).to(device)

            logits = model(input_ids)
            loss = criterion(logits.squeeze(), label.squeeze())
            total_loss += loss.item()

    avg_loss = total_loss / len(dev_data)
    return avg_loss

for epoch in range(5):
    train_loss = train(model, train_data)
    dev_loss = evaluate(model, dev_data)
    print(f"Epoch {epoch+1}")
    print(f"  Train Loss: {train_loss:.4f}")
    print(f"  Dev Loss  : {dev_loss:.4f}")
