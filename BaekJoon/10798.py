# 2025년 5월 1일
# 백준 10798번

matrix = [[None for _ in range(15)] for __ in range(5)]

def read_lines() :
    line = input()
    return [letter for letter in line]

for matrix_row in matrix :
    line = read_lines()
    for j in range(len(matrix_row)) :
        try :
            matrix_row[j] = line[j]
        except :
            continue

for i in range(15) :
    for matrix_row in matrix :
        if matrix_row[i] != None :
            print(matrix_row[i], end = '')
        else :
            continue
        