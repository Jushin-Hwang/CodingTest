# 2024년 9월 2일
# 백준 10809번

S = input()

alphabet = [-1] * 26

for i in range(len(S)) :
    if alphabet[ord(S[i]) - 97] == -1 :
        alphabet[ord(S[i]) - 97] = i

for i in range(26) :
    print(alphabet[i], end = ' ')