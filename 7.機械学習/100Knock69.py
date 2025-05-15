# 69.正則化パラメータの変更
C_values = [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000]
accuracies = []

for C in C_values:
    model = LogisticRegression(C=C, max_iter=1000)
    model.fit(X_train, train_labels)
    y_pred = model.predict(X_dev)
    acc = accuracy_score(dev_labels, y_pred)
    accuracies.append(acc)
    print(f"C={str(C).ljust(6)}, Accuracy={acc:.4f}")

plt.figure(figsize=(8, 6))
plt.plot(C_values, accuracies, marker="o")
plt.xscale("log")
plt.grid(True)
plt.title("Relationship between Regularization Parameter and Accuracy Rate")
plt.xlabel("Regularization Parameter (C)")
plt.ylabel("Accuracy")
plt.tight_layout()
plt.show()
