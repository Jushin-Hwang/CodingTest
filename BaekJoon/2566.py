# 2025년 5월 1일
# 백준 2566번

def input_int_lines() :
    return [int(num) for num in list(input().split(' '))]

matrix = [[0 for _ in range(9)] for __ in range(9)]

for i in range(9) :
    int_lines = input_int_lines()
    for j in range(9) :
        matrix[i][j] = int_lines[j]

max = -1
x = -1
y = -1
for matrix_row in matrix :
    for number in matrix_row :
        if number > max :
            max = number
            y = matrix_row.index(number)
            x = matrix.index(matrix_row)
        else :
            continue

print(max)
print(x + 1, y + 1)