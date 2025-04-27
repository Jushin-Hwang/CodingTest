# 2025년 4월 26일
# 백준 10951번
import sys

def get_numbers() :
    a = sys.stdin.readline().rstrip()
    a_list = [int(number) for number in a.split(' ')]    
    return a_list

while(True) : # EOF일 때까지 Sum 출력
    try :
        num_list = get_numbers()
        print(num_list[0] + num_list[1])
    except :
        break
