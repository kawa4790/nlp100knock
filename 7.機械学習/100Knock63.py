# 63.予測
with open('./model/logistic_regression_model.pkl', 'rb') as f:
    model = pickle.load(f)
y_pred = model.predict(X_dev[0])[0]
print(f"text：{dev_list[0]['text']}")
print(f"pred_label：{y_pred}")
print(f"gold_label：{dev_labels[0]}")
