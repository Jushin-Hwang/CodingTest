# 2025년 5월 10일
# 백준 3009번

coordinates_x = []
coordinates_y = []

for i in range(3) :
    numbers = input().split(' ')
    x = int(numbers[0])
    y = int(numbers[1])
    coordinates_x.append(x)
    coordinates_y.append(y)

set_x = set(coordinates_x)
set_y = set(coordinates_y)

for x_ in set_x :
    if coordinates_x.count(x_) == 1 :
        result_x = x_
        break

for y_ in set_y :
    if coordinates_y.count(y_) == 1 :
        result_y = y_
        break

print(f"{result_x} {result_y}")
