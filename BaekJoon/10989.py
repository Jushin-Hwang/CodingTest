# 2025년 6월 3일 
# 백준 10989번

# N 입력받기
N = int(input())

N_list = []
for i in range(N) :
    N_list.append(int(input()))

N_list.sort()

for i in range(N) :
    print(N_list[i])