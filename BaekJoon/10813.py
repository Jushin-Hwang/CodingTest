# 2025년 4월 26일
# 백준 10813번
import sys

def get_number() :
    a = sys.stdin.readline().rstrip()
    a_int = int(a)
    return a_int

def get_numbers() :
    a = sys.stdin.readline().rstrip()
    a_list = [int(number) for number in a.split(' ')]    
    return a_list

N_M_list = get_numbers()
N = N_M_list[0] # N 입력받기
M = N_M_list[1] # M 입력받기

bucket_list = [i + 1 for i in range(N)] # 바구니 리스트 만들기

for i in range(M) :
    num_list = get_numbers() # number 받아서 list에 저장
    num1 = num_list[0] - 1
    num2 = num_list[1] - 1
    temp = bucket_list[num1] # num1번 바구니와 num2번 바구니의 값 swap
    bucket_list[num1] = bucket_list[num2]
    bucket_list[num2] = temp

for bucket in bucket_list :
    print(bucket, end = ' ') # 결과 출력