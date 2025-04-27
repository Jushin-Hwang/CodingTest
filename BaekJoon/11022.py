# 2025년 4월 26일
# 백준 11022번
import sys

def get_number() :
    a = sys.stdin.readline().rstrip()
    a_int = int(a)
    return a_int

def get_numbers() :
    a = sys.stdin.readline().rstrip()
    a_list = [int(number) for number in a.split(' ')]    
    return a_list

T = get_number() # Test Case 입력받기
for i in range(T) :
    number_list = get_numbers() # A, B 입력받기
    print(f"Case #{i + 1}: {number_list[0]} + {number_list[1]} = {number_list[0] + number_list[1]}") # 결과 출력