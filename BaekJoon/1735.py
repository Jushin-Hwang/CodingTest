# 2025년 6월 22일
# 백준 1735번

def GCD(a, b) :
    if a == b :
        return a
    elif a == 0 :
        return b
    elif b == 0 :
        return a
    
    if a > b :
        return GCD(b, a % b)
    else :
        return GCD(a, b % a)

def solution(a, b, c, d) :
    numerator = (a * d) + (c * b)
    denominator = (b * d)
    gcd = GCD(numerator, denominator)
    print(numerator // gcd, denominator // gcd)
    return


a, b = map(int, input().split())
c, d = map(int, input().split())
solution(a, b, c, d)