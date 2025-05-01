# 2025년 5월 1일
# 백준 2903번

N = int(input())

number = 2
for _ in range(N) :
    number += (number - 1)

print(number ** 2)