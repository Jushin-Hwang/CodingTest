# 2025년 4월 26일
# 백준 3052번
import sys

def get_number() :
    a = sys.stdin.readline().rstrip()
    a_int = int(a)
    return a_int

def get_numbers() :
    a = sys.stdin.readline().rstrip()
    a_list = [int(number) for number in a.split(' ')]    
    return a_list

remain_list = [] # 나머지 저장할 리스트 선언
for i in range(10) :
    number = get_number() # number 입력받기
    remain_list.append(number % 42) # 42로 나눈 나머지 저장

remain_list = set(remain_list) # 중복 값 삭제
print(len(remain_list)) # remain_list의 len값 출력