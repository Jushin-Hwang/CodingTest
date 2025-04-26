# 2025년 4월 26일
# 백준 11382번

def get_numbers() :
    A, B, C = input().split(' ')
    A, B, C = int(A), int(B), int(C)
    return A, B, C

A, B, C = get_numbers() # A, B, C 입력받기
print(A + B + C) # A + B + C 출력
