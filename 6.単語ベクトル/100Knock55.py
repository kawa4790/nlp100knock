# 55.アナロジータスクでの正解率
sementic_total = 0
semantic_correct = 0
syntactic_total = 0
syntactic_correct = 0

file = "questions-words-analogy.txt"

with open(file, 'r') as f:
    for line in f:
        category, true_line, predicted_word = line.strip().split('\t')
        true_word = true_line.split()[3]

        if category.startswith('gram'):
            syntactic_total += 1
            if predicted_word == true_word:
                syntactic_correct += 1
        else:
            semantic_total += 1
            if predicted_word == true_word:
                semantic_correct += 1

print(f"意味的アナロジーの正解率：{semantic_correct / semantic_total:.4f}")
print(f"文法的アナロジーの正解率：{syntactic_correct / syntactic_total:.4f}")