# 44.係り受け木の可視化
import graphviz
from IPython.display import display


def visualize_dependency_tree(sentence, sentence_id=0):
    dot = graphviz.Digraph(comment=f"Dependency Tree {sentence_id}", format="png")
    dot.attr("node", shape="box")  # fontname属性を削除
    
    for i, chunk in enumerate(sentence):
        chunk_text = str(chunk)
        dot.node(f"{i}", chunk_text)
    
    for i, chunk in enumerate(sentence):
        if chunk.dst != -1:
            dot.edge(f"{i}", f"{chunk.dst}")
    
    return dot


parsed_chunks = load_chunks('ai.ja.txt.parsed')
first_sentence = parsed_chunks[1]
visualize_dependency_tree(first_sentence, 'first_sentence_dep_tree')