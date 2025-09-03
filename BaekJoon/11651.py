# 2025년 6월 7일
# 백준 11651번

import sys

# N 입력받기
N = int(sys.stdin.readline())

# N의 갯수만큼 좌표 입력받아 배열에 저장하기
co_list = []
for _ in range(N) :
    x, y = map(int, sys.stdin.readline().split(' '))
    co_list.append([x, y])

# 리스트 정렬하기
co_list.sort(key = lambda coord : (coord[1], coord[0]))

# 정렬된 리스트 출력하기
for coordinate in co_list :
    print(coordinate[0], coordinate[1])
