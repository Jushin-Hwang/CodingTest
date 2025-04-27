# 2025년 4월 26일
# 백준 10807번
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
num_list = get_numbers() # 숫자 리스트 입력받기
v = get_number() # v 입력받기

count = 0 # count 초기화
for num in num_list : # num_list에서 num을 추출해서 v와 같을 경우, count 1씩 증가
    if num == v :
        count += 1

print(count) # 결과 출력