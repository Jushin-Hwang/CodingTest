# 2025년 6월 20일
# 백준 1934번

'''
9월 9일 오답노트 1 : 시간초과 발생.
유클리드 호제법이라는 알고리즘을 발견했음. 이를 활용하여 문제를 풀어보자.
'''

T = int(input())

def GCD(a, b) :
    if a == 0 :
        return b
    elif b == 0 :
        return a

    if a > b :
        return GCD(b, a % b)
    elif a < b :
        return GCD(a, b % a)

for _ in range(T) :
    a, b = map(int, input().split())
    if a == b :
        print(a)
    else :
        print(a * b // GCD(a, b))