# 67.精度の計測
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
def evaluate_metrics(y_true, y_pred):
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred)
    rec = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    print(f"正解率：{acc:.4f}")
    print(f"適合率：{prec:.4f}")
    print(f"再現率：{rec:.4f}")
    print(f"F1スコア：{f1:.4f}\n")

with open('./model/logistic_regression_model.pkl', 'rb') as f:
    model = pickle.load(f)

train_pred = model.predict(X_train)
dev_pred = model.predict(X_dev)

print("学習データ")
evaluate_metrics(train_labels, train_pred)

print("検証データ")
evaluate_metrics(dev_labels, dev_pred)
