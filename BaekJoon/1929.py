# 2025년 6월 25일
# 백준 1929번

import sys
import math

def is_prime(num) :
    if num == 1 :
        return False
    elif num == 2 :
        return True
    else :
        for i in range(2, int(math.sqrt(num)) + 1) :
            if num % i == 0 :
                return False
        return True

N, M = map(int,sys.stdin.readline().split())

for i in range(N, M + 1) :
    if is_prime(i) :
        print(i)

