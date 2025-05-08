# 58.Ward法によるクラスタリング
import pycountry
from sklearn.decomposition import PCA
from scipy.cluster.hierarchy import linkage, dendrogram
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

# 階層型クラスタリング
linkage_matrix = linkage(vectors, method='ward')

# デンドログラムの描画
plt.figure(figsize=(15, 8))
dendrogram(linkage_matrix, labels=country_names, leaf_rotation=90, leaf_font_size=10)
plt.xlabel("Country")
plt.ylabel("Distance")
plt.tight_layout()
plt.show()
