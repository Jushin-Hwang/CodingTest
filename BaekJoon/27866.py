# 2025년 4월 27일
# 백준 27866번
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
i = get_number() # 정수 i 입력받기
print(S[i - 1]) # S의 i번째 글자를 출력