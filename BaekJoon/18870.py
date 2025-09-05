# 2025년 6월 11일
# 백준 18870번

'''
0905 오답노트 1 : 시간초과 발생.
기존 index() 함수를 쓰지 않고, dictionary를 사용해서 시간 복잡도를 줄여보기로 함.
'''

# N 입력받기
N = int(input())

# 좌표 입력받기
coor = list(map(int, input().split()))

# 비교대상 만들기
sorted_setted_coor = sorted(list(set(coor)))

# 딕셔너리 만들기
dict_coor = {}
for i in range(len(sorted_setted_coor)) :
    dict_coor[sorted_setted_coor[i]] = i

# 결과 출력하기
for item in coor :
    print(dict_coor[item], end = ' ')