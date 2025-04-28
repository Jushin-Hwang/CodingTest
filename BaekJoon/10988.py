# 2025년 4월 28일
# 백준 10988번

word = input()

len_word = len(word)

def solution(word) :
    for i in range(len_word // 2) :
        if word[i] != word[-(i+1)] :
            return 0
    return 1

print(solution(word))