# 2025년 4월 28일
# 백준 3003번

chess_units = [1, 1, 2, 2, 2, 8]
remain_units = [int(item) for item in input().split(' ')]
result_units = []

for i in range(6) :
    result_units.append(chess_units[i] - remain_units[i])

for result_unit in result_units :
    print(result_unit, end = " ")
