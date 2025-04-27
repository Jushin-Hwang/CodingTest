# 2025년 4월 26일
# 백준 2562번
import sys

def get_number() :
    a = sys.stdin.readline().rstrip()
    a_int = int(a)
    return a_int

def get_numbers() :
    a = sys.stdin.readline().rstrip()
    a_list = [int(number) for number in a.split(' ')]    
    return a_list

num_list = []
for i in range(9) :
    num_list.append(get_number()) # 9번 숫자 입력받아서 리스트에 저장

max_number = max(num_list) # max값 구하기
index = num_list.index(max_number) # max값의 인덱스 구하기
print(max_number) # max값 출력
print(index + 1) # index값 출력