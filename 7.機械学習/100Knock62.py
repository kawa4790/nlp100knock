# 62.学習
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

train_features = [item["feature"] for item in train_list]
train_labels = [item["label"] for item in train_list]

dev_features = [item["feature"] for item in dev_list]
dev_labels = [item["label"] for item in dev_list]

# sklearnで学習できるように、sparse matrixに変換
vec = DictVectorizer()
X_train = vec.fit_transform(train_features)
X_dev = vec.transform(dev_features)

# ロジスティック回帰モデルの学習
model = LogisticRegression(max_iter=1000)
model.fit(X_train, train_labels)

# 学習モデルの保存
with open("./model/logistic_regression_model.pkl", mode="wb") as f:
    pickle.dump(model, f, protocol=2)
