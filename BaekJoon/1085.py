# 2025년 5월 9일
# 백준 1085번

numbers = input().split(' ')
x = int(numbers[0])
y = int(numbers[1])
w = int(numbers[2])
h = int(numbers[3])

distance_left = x
distance_right = w - x
distance_up = h - y
distance_down = y

print(min([distance_left, distance_down, distance_right, distance_up]))