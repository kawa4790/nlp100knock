# 65.テキストのポジネガの予測
def predict_posi_nega(model,text):
    model=model
    tokens = text.split()
    feature_vec = dict(Counter(tokens))
    transform = vec.transform(feature_vec)
    pred = model.predict(transform)[0]
    return "positive" if pred == 1 else "negative"

with open('./model/logistic_regression_model.pkl', 'rb') as f:
    model = pickle.load(f)

text = "the worst movie I 've ever seen"
print(predict_posi_nega(model,text))
