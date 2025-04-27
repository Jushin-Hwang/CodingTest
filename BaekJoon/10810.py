# 2025년 4월 26일
# 백준 10810번
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

bucket_list = [0 for i in range(N)] # 바구니 리스트 만들기
for i in range(M) :
    num_list = get_numbers() # number list 입력받기
    start = num_list[0] - 1
    end = num_list[1] - 1
    ball = num_list[2] 
    bucket_list[start:end + 1] = [ball] * (end - start + 1) # start부터 end번 바구니까지 ball번 공 담기

for bucket in bucket_list :
    print(bucket, end = " ") # 결과 출력