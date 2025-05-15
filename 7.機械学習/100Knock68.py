# 68.特徴量の重みの確認

import numpy as np

feature_names = vec.get_feature_names_out()

weights = model.coef_[0]

top20= np.argsort(weights)[-20:][::-1]  
bottom20 = np.argsort(weights)[:20]      

print("重みの高い特徴量トップ20:")
for i in top20_idx:
    print(f"{feature_names[i]:<20} {weights[i]:.4f}")

print("\n重みの低い特徴量トップ20:")
for i in bottom20_idx:
    print(f"{feature_names[i]:<20} {weights[i]:.4f}")
