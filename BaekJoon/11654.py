# 2025년 4월 27일
# 백준 11654번
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
print(ord(S)) # S의 아스키코드값 출력