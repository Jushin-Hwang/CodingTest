# 2025년 4월 26일
# 백준 10430번

def get_numbers() :
    A, B, C = input().split(' ')
    A, B, C = int(A), int(B), int(C)
    return A, B, C

A, B, C = get_numbers() # 숫자 입력받기

print((A + B) % C) # 첫번째 출력
print(((A % C) + (B % C)) % C) # 두번째 출력
print((A * B) % C) # 세번째 출력
print(((A % C) * (B % C)) % C) # 네번째 출력