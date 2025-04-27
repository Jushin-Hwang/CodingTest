# 2025년 4월 27일
# 백준 2743번
import sys

def get_number() :
    a = sys.stdin.readline().rstrip()
    a_int = int(a)
    return a_int

def get_numbers() :
    a = sys.stdin.readline().rstrip()
    a_list = [int(number) for number in a.split(' ')]    
    return a_list

S = input() # 문자열 S 입력받기
print(len(S)) # S의 len값 출력