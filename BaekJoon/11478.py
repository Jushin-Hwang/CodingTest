# 2025년 6월 19일
# 백준 11478번

word = input()

word_set = set()
for i in range(0, len(word)) :
    for j in range(0, len(word) - i + 1) :
        word_set.add(word[i:i+j])

word_set.remove('')
print(len(word_set))