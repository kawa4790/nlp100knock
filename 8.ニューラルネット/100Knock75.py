# 75.パディング
# 75.パディング
import torch
from torch.nn.utils.rnn import pad_sequence

def collate(data):
    # トークン列の長さで降順ソート
    data = sorted(data, key=lambda x: len(x["input_ids"]), reverse=True)

    # input_idsとlabelを分離
    input_ids_list = [item["input_ids"] for item in data]
    labels_list = [item["label"] for item in data]

    # パディング（0番のIDで揃える）
    padded_input_ids = pad_sequence(input_ids_list, batch_first=True, padding_value=0)

    # ラベルもテンソル結合
    labels = torch.stack(labels_list)

    return {"input_ids": padded_input_ids, "label": labels}

padded_data = collate(train_data[0:4])
print(padded_data)
