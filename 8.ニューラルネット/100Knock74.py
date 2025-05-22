# 74.モデルの評価
def compute_accuracy(model, data):
    model.eval()
    correct = 0
    total = 0

    with torch.no_grad():
        for example in data:
            input_ids = example["input_ids"].unsqueeze(0).to(device)  
            label = example["label"].item()                            
            logits = model(input_ids)                                  
            probs = torch.sigmoid(logits).item()                       
            pred_label = 1.0 if probs >= 0.5 else 0.0

            if pred_label == label:
                correct += 1
            total += 1

    return correct / total

accuracy = compute_accuracy(model, dev_data)
print(f"正解率: {accuracy:.4f}")