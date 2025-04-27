# 2025년 4월 26일
# 백준 10952번
import sys

def get_numbers() :
    a = sys.stdin.readline().rstrip()
    a_list = [int(number) for number in a.split(' ')]    
    return a_list

number_list = get_numbers() # 숫자 입력받기

while(number_list[0] != 0 or number_list[1] != 0) : # 입력받은 두개의 숫자가 모두 0이 아닌 경우
    print(number_list[0] + number_list[1]) # 결과 출력
    number_list = get_numbers()