# 41.係り受け解析結果の読み込み（文節・係り受け）
class Chunk:
    def __init__(self, morphs=None, dst=-1):
        self.morphs = morphs if morphs else []
        self.dst = dst
        self.srcs = []

    def surface(self):
        return ''.join(m.surface for m in self.morphs if m.pos != '記号')

    def __repr__(self):
        return f"surface: {self.surface()}, dst: {self.dst}, srcs: {self.srcs}"

def load_chunks(filename):
    sentences = []
    chunks = {}
    idx = -1

    with open(filename, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line == 'EOS':
                if chunks:
                    # srcs を構築
                    for i, chunk in chunks.items():
                        if chunk.dst != -1:
                            chunks[chunk.dst].srcs.append(i)
                    sentences.append([chunks[i] for i in sorted(chunks)])
                    chunks = {}
                continue

            if line.startswith('*'):
                # 文節開始
                cols = line.split()
                idx = int(cols[1])
                dst = int(cols[2].rstrip('D'))
                chunks[idx] = Chunk(morphs=[], dst=dst)
            else:
                surface, attr = line.split('\t')
                attr = attr.split(',')
                morph = Morph(
                    surface=surface,
                    base=attr[6],
                    pos=attr[0],
                    pos1=attr[1]
                )
                chunks[idx].morphs.append(morph)

    return sentences

parsed_chunks = load_chunks('ai.ja.txt.parsed')

for i, chunk in enumerate(parsed_chunks[1]):
    print(f"[{i}] {chunk.surface()} -> {chunk.dst}")