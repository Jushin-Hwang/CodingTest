# 2025년 4월 26일
# 백준 10950번

def get_numbers() :
    a = [int(number) for number in input().split(' ')]
    return a

def get_number() :
    a = int(input())
    return a

T = get_number() # Test Case 갯수 입력받기
for i in range(T) :
    number_list = get_numbers() # Test Case 입력받기
    A = number_list[0]
    B = number_list[1]
    print(A + B) # 합한 값 출력