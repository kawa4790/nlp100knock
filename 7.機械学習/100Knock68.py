# 68.特徴量の重みの確認
import numpy as np
import pandas as pd

# 特徴量名と重みを取得
feature_names = vec.get_feature_names_out()
weights = model.coef_[0]

feature_weights = pd.DataFrame({
    'Feature': feature_names,
    'Weight': weights
})

top_features = feature_weights.sort_values(by='Weight', ascending=False).head(20)
bottom_features = feature_weights.sort_values(by='Weight', ascending=True).head(20)

def show_feature_table(df, title):
    print(f"\n{title}")
    print(df.to_string(index=False))

show_feature_table(top_features, "重みの高い特徴量トップ20")
show_feature_table(bottom_features, "重みの低い特徴量トップ20")
