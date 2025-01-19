# 16.ファイルをN分割する
import numpy as np
N = int(input())
with open('../NLP100Knock/popular-names.txt', 'r') as f:
    lines = f.readlines()
    count = len(lines)
    nums = range(count)
    div = np.array_split(nums, N)
    for i, div in enumerate(div, 1):
        f = open('{}.txt'.format(str(i).zfill(3)), 'w')
        for j in div:
            f.write(lines[j])
        f.close()
        
# split -n l/3 popular-names.txt