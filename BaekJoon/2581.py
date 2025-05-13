# 2025년 5월 6일
# 백준 2581번

N = int(input())
M = int(input())

primes = []
for number in range(N, M + 1) :
    factors = []
    is_prime = True
    for i in range(2, number) :
        if number % i == 0 :
            is_prime = False
            break
    if number == 1 :
        is_prime = False
    if is_prime :
        primes.append(number)
        
if primes :
    print(sum(primes))
    print(min(primes))
else :
    print(-1)