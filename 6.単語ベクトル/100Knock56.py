# 56.WorldSimilarity-353での評価
from scipy.stats import spearmanr
import pandas as pd

df = pd.read_csv("wordsim353/combined.csv")
human_scores = []
model_scores = []

for _, row in df.iterrows():
    w1, w2 = row['Word 1'], row['Word 2']
    try:
        sim = model.similarity(w1, w2)
        model_scores.append(sim)
        human_scores.append(row['Human (mean)'])
    except KeyError:
        continue

corr, _ = spearmanr(human_scores, model_scores)
print(f"スピアマン相関係数: {corr:.4f}")