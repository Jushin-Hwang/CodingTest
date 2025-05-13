# 2025년 5월 5일
# 백준 1978번

N = int(input())

numbers = input().split(' ')

count = 0
for number in numbers :
    number = int(number)
    factors = []
    for i in range(1, number + 1) :
        if number % i == 0 :
            factors.append(i)
    if len(factors) == 2 :
        count += 1

print(count)