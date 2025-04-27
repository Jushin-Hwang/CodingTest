# 2025년 4월 26일
# 백준 10817번
import sys

def get_numbers() :
    a = sys.stdin.readline().rstrip()
    a_list = [int(number) for number in a.split(' ')]    
    return a_list

num_list = get_numbers() # num_list 입력
num_list.sort() # num_list 정렬
print(num_list[1]) # 결과 출력