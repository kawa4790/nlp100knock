# 66.混同行列の作成
from sklearn.metrics import confusion_matrix
from matplotlib import pyplot as plt

def plot_confusion_matrix(y_true, y_pred, labels=None, title="Confusion Matrix", cmap=plt.cm.Blues):
    confmat = confusion_matrix(y_true=y_true, y_pred=y_pred, labels=labels)
    
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.matshow(confmat, cmap=cmap, alpha=0.7)

    for i in range(confmat.shape[0]):
        for j in range(confmat.shape[1]):
            ax.text(x=j, y=i, s=confmat[i, j], va="center", ha="center", fontsize=12)

    ax.set_xlabel("Predicted label", fontsize=12)
    ax.set_ylabel("True label", fontsize=12)
    ax.set_title(title, fontsize=14)
    ax.xaxis.set_ticks_position("bottom")

    plt.tight_layout()
    plt.show()

# モデル読み込みと予測
with open('./model/logistic_regression_model.pkl', 'rb') as f:
    model = pickle.load(f)

dev_pred = model.predict(X_dev)

# 混同行列の描画
plot_confusion_matrix(dev_labels, dev_pred)
