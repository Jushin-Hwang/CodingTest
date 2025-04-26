# 2025년 4월 26일
# 백준 10869번

def get_num() :
    A, B = input().split(' ')
    A, B = int(A), int(B)
    return A, B

A, B = get_num()

print(A + B) # 덧셈 값
print(A - B) # 뺄셈 값
print(A * B) # 곱셈 값
print(A // B) # 몫
print(A % B) # 나머지