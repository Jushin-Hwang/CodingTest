# 2025년 6월 24일
# 백준 4134번

import sys
import math

def is_prime(num) :
    for i in range(2, int(math.sqrt(num)) + 1) :
        if num % i == 0 :
            return False
    return True

def next_prime(number) :
    if is_prime(number) :
        return number
    else :
        return next_prime(number + 1)

N = int(sys.stdin.readline())

for _ in range(N) :
    number = int(sys.stdin.readline())
    if number <= 1 :
        print(2)
    else:
        print(next_prime(number))

