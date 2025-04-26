def get_num() :
    A, B = input().split(' ')
    A, B = int(A), int(B)
    return A, B

A, B = get_num()
print(A / B)