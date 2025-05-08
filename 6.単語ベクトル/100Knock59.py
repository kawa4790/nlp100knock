# 59.t-SNEによる可視化
import pycountry
from gensim.models import KeyedVectors
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import numpy as np

country_names = []
vectors = []

for country in pycountry.countries:
    name = country.name.replace(" ", "_")  
    try:
        vec = model[name]
        country_names.append(name)
        vectors.append(vec)
    except KeyError:
        continue

vectors = np.array(vectors)

tsne = TSNE(n_components=2, random_state=42, perplexity=30, n_iter=1000)
reduced = tsne.fit_transform(vectors)

plt.figure(figsize=(16, 10))
plt.scatter(reduced[:, 0], reduced[:, 1], s=30, alpha=0.6)

for i, label in enumerate(country_names):
    plt.text(reduced[i, 0] + 0.5, reduced[i, 1] + 0.5, label, fontsize=8)

plt.grid(True)
plt.tight_layout()
plt.show()
