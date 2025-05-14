# 2025년 5월 12일
# 백준 9063번

N = int(input())

x_list = []
y_list = []
for i in range(N) :
    numbers = input().split(' ')
    x_list.append(int(numbers[0]))
    y_list.append(int(numbers[1]))

min_x = min(x_list)
max_x = max(x_list)
min_y = min(y_list)
max_y = max(y_list)

width = max_x - min_x
height = max_y - min_y

print(width * height)