# 2025년 5월 3일
# 백준 2501번

numbers = input().split(' ')
num1 = int(numbers[0])
num2 = int(numbers[1])

factors = []

for i in range(1, num1 + 1) :
    if num1 % i == 0 :
        factors.append(i)

try :
    print(factors[num2 - 1])
except :
    print(0)