# 2025년 6월 13일
# 백준 14425번

N, M = map(int, input().split())

word_list = []
for i in range(N) :
    word_list.append(input())

cnt = 0
for _ in range(M) :
    test_word = input()
    if test_word in word_list :
        cnt += 1

print(cnt)