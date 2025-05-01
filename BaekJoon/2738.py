# 2025년 5월 1일
# 백준 2738번

def input_list() :
    return list(input().split(' '))

N_M_list = input_list()
N = int(N_M_list[0])
M = int(N_M_list[1])

matrix_A = [[0 for i in range(M)] for j in range(N)]
matrix_B = [[0 for i in range(M)] for j in range(N)]

def make_matrix(matrix) :
    for i in range(N) :
        matrix_list = input_list()
        for j in range(M) :
            matrix[i][j] = int(matrix_list[j])

make_matrix(matrix_A)
make_matrix(matrix_B)

for i in range(N) :
    for j in range(M) :
        matrix_A[i][j] += matrix_B[i][j]
        print(matrix_A[i][j], end = ' ')
    print()

