# 2025년 6월 6일
# 백준 11650번
'''
0903 오답노트 1 : 시간초과 발생!
점의 개수 N (1 ≤ N ≤ 100,000) 때문에 발생하는 문제가 아닐까?
sys.stdin.readline()을 사용해보기로 함.

0903 오답노트 2 : 여전히 시간초과 발생!
sort()함수에 key 매개변수가 있음을 확인.
key 매개변수를 사용해서 문제를 해결해보자!
'''
import sys

# N 입력받기
N = int(sys.stdin.readline())

# N의 갯수만큼 좌표 입력받아 배열에 저장하기
co_list = []
for _ in range(N) :
    x, y = map(int, sys.stdin.readline().split(' '))
    co_list.append([x, y])

# 리스트 정렬하기
co_list.sort(key = lambda coord : (coord[0], coord[1]))

# 정렬된 리스트 출력하기
for coordinate in co_list :
    print(coordinate[0], coordinate[1])
