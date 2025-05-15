# 64.条件付き確率
pro = model.predict_proba(X_dev[0])

print(f'0: {pro[0][0]}')
print(f'1: {pro[0][1]}')
