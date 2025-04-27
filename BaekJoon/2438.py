# 2025년 4월 26일
# 백준 2438번
import sys

def get_number() :
    a = sys.stdin.readline().rstrip()
    a_int = int(a)
    return a_int

N = get_number() # N 입력받기
for i in range(N) :
    print('*' * (i + 1)) # 별 찍기