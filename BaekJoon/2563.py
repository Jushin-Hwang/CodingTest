# 2025년 5월 1일
# 백준 2563번

matrix = [[0 for _ in range(100)] for __ in range(100)]

number_of_paper = int(input())

def put_paper(start_x, start_y) :
    for y in range(start_y, start_y + 10) :
        for x in range(start_x, start_x + 10) :
            matrix[y][x] = 1

def solution() :
    coordinate = [int(number) for number in input().split(' ')]
    x = coordinate[0]
    y = coordinate[1]
    put_paper(x, y)

for _ in range(number_of_paper) :
    solution()

count = 0
for matrix_row in matrix :
    for item in matrix_row :
        if item == 1 :
            count += 1
        else :
            continue

print(count)