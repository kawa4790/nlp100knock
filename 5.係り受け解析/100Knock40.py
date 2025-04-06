# 40.係り受け解析結果の読み込み（形態素）
class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __repr__(self):
        return f"surface: {self.surface}, base: {self.base}, pos: {self.pos}, pos1: {self.pos1}"

def load_morphs(filename):
    sentences = []
    morphs = []

    with open(filename, encoding='utf-8') as f:
        for line in f:
            if line == 'EOS\n':
                if morphs:
                    sentences.append(morphs)
                    morphs = []
            elif line.startswith('*'):
                continue  
            else:
                surface, attr = line.split('\t')
                attr = attr.split(',')
                morph = Morph(
                    surface=surface,
                    base=attr[6],
                    pos=attr[0],
                    pos1=attr[1]
                )
                morphs.append(morph)

    return sentences

parsed_sentences = load_morphs('ai.ja.txt.parsed')

for morph in parsed_sentences[1]:
    print(morph)