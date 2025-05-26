# 2025년 5월 15일 
# 백준 14215번
numbers = [int(number) for number in input().split(' ')]
max_num = max(numbers)
numbers.remove(max_num)

if max_num >= sum(numbers) :
    max_num = sum(numbers) - 1

print(max_num + sum(numbers))