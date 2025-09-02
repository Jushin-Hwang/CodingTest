# 2025년 6월 2일 
# 백준 2751번
import sys

# N 입력받기
N = int(sys.stdin.readline())

# N개의 줄만큼 숫자 입력받기
N_list = []
for _ in range(N) :
    N_list.append(int(sys.stdin.readline()))

N_list.sort()

for i in range(N) :
    print(N_list[i])