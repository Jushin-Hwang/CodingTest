# 2025년 4월 26일
# 백준 10871번
import sys

def get_number() :
    a = sys.stdin.readline().rstrip()
    a_int = int(a)
    return a_int

def get_numbers() :
    a = sys.stdin.readline().rstrip()
    a_list = [int(number) for number in a.split(' ')]    
    return a_list

N_X_list = get_numbers()
N = N_X_list[0] # N 입력받기
X = N_X_list[1] # X 입력받기
list_A = get_numbers() # A list 입력받기

result_list = []
for number in list_A : # list의 요소가 X보다 작을 경우, result_list에 추가
    if number < X :
        result_list.append(number)

for result in result_list :
    print(result, end = " ") # 결과 출력