# 71.データセットの読み込み
import csv
import torch

def load_sst_dataset(filepath, word_to_id):
    dataset = []

    with open(filepath, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            text = row['sentence'].strip()
            label = float(row['label'])

            # トークン列に変換（語彙にある単語のみ）
            tokens = text.split()
            token_ids = [word_to_id[word] for word in tokens if word in word_to_id]

            # 語彙に1語も含まれなければスキップ
            if not token_ids:
                continue

            entry = {
                "text": text,
                "label": torch.tensor([label], dtype=torch.float32),
                "input_ids": torch.tensor(token_ids, dtype=torch.long),
            }
            dataset.append(entry)

    return dataset

train_path = "/home/j138kawa/NLP100Knock/SST-2/train.tsv"
dev_path = "/home/j138kawa/NLP100Knock/SST-2/dev.tsv"

train_data = load_sst_dataset(train_path, word_to_id)
dev_data = load_sst_dataset(dev_path, word_to_id)

print(f"Filtered train size: {len(train_data)}")
print(f"Filtered dev size: {len(dev_data)}")

print(train_data[0])