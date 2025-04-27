# 2025년 4월 27일
# 백준 9086번
import sys

def get_number() :
    a = sys.stdin.readline().rstrip()
    a_int = int(a)
    return a_int

def get_numbers() :
    a = sys.stdin.readline().rstrip()
    a_list = [int(number) for number in a.split(' ')]    
    return a_list

T = get_number() # Test Case 갯수 입력받기

for i in range(T) :
    S = input() # S 입력받기
    print(f"{S[0]}{S[-1]}") # 결과 출력