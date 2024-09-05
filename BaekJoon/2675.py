# 2024년 9월 3일 
# 백준 2675번
# 수정 1) solution 함수에서 하나의 output 이후에 줄바꿈을 해주도록 수정

T = int(input())

def solution() :
    R, S = input().split()
    R = int(R)

    for i in range(len(S)) :
        for _ in range(R) :
            print(S[i], end = '')
    print()

for __ in range(T) :
    solution()