# 2025년 6월 21일
# 백준 13241번

def GCD(a, b) :
    if a == 0 :
        return b
    elif b == 0 :
        return a

    if a > b :
        return GCD(b, a % b)
    elif a < b :
        return GCD(a, b % a)

a, b = map(int, input().split())
if a == b :
    print(a)
else :
    print(a * b // GCD(a, b))