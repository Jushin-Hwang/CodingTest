# 2025년 4월 26일
# 백준 10811번
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

bucket_list = [ i + 1 for i in range(N)] # 바구니 리스트 선언

for i in range(M) :
    num_list = get_numbers()
    start = num_list[0] - 1
    end = num_list[1] - 1
    for j in range((end - start + 1) // 2) : # 역순으로 재배치
        temp = bucket_list[start + j]
        bucket_list[start + j] = bucket_list[end - j]
        bucket_list[end - j] = temp

for bucket in bucket_list :
    print(bucket, end = ' ') # 결과 출력