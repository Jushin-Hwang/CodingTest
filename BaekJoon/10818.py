# 2025년 4월 26일
# 백준 10818번
import sys

def get_number() :
    a = sys.stdin.readline().rstrip()
    a_int = int(a)
    return a_int

def get_numbers() :
    a = sys.stdin.readline().rstrip()
    a_list = [int(number) for number in a.split(' ')]    
    return a_list

N = get_number() # N 입력받기
if N > 0 :
    num_list = get_numbers() # 숫자 리스트 입력받기

print(f"{min(num_list)} {max(num_list)}") # 리스트 중 min값과 max값 출력하기