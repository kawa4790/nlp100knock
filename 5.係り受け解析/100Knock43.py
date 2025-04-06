# 43.名詞を含む文節が動詞を含む文節に係るものを抽出
def has_pos(chunk, pos):
    return any(m.pos == pos for m in chunk.morphs)

def extract_noun_to_verb(sentences):
    for chunks in sentences:
        for chunk in chunks:
            if chunk.dst != -1:
                dst_chunk = chunks[chunk.dst]
                # 名詞 → 動詞 の関係があるときのみ出力
                if has_pos(chunk, '名詞') and has_pos(dst_chunk, '動詞'):
                    src_text = chunk.surface()
                    dst_text = dst_chunk.surface()
                    if src_text and dst_text:
                        print(f"{src_text}\t{dst_text}")

parsed_chunks = load_chunks('ai.ja.txt.parsed')
extract_noun_to_verb(parsed_chunks)