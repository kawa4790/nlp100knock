# 57.k-meansクラスタリング
import numpy as np
import pycountry
from sklearn.cluster import KMeans
from collections import defaultdict

country_set = set()
for country in pycountry.countries:
    name = country.name.replace(" ", "_")  # Word2Vec形式に合わせる（例: United States → United_States）
    country_set.add(name)

country_vecs = []
valid_countries = []

for country in country_set:
    try:
        vec = model[country]
        country_vecs.append(vec)
        valid_countries.append(country)
    except KeyError:
        continue  

country_vecs = np.array(country_vecs)

k = 5
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
labels = kmeans.fit_predict(country_vecs)

clusters = defaultdict(list)
for country, label in zip(valid_countries, labels):
    clusters[label].append(country)

# 結果表示
for label, countries in clusters.items():
    print(f"\nCluster {label}:")
    print(", ".join(sorted(countries)))