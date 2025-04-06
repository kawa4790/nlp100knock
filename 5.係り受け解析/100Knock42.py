# 42.係り元と係り先の文節の表示
def extract_dependency_relations(sentences):
    for chunks in sentences:
        for chunk in chunks:
            if chunk.dst != -1:
                src = chunk.surface()
                dst = chunks[chunk.dst].surface()
                if src and dst:
                    print(f"{src}\t{dst}")

parsed_chunks = load_chunks('ai.ja.txt.parsed')
extract_dependency_relations(parsed_chunks)