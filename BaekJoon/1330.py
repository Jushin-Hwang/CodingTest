# 2025년 4월 26일
# 백준 1330번

def get_numbers() :
    a, b  = input().split(' ')
    a, b = int(a), int(b)
    return a, b

A, B = get_numbers() # 숫자 입력받기

if A > B :
    print('>') # A가 B보다 클 경우
elif A < B :
    print('<') # A가 B보다 작을 경우
elif A == B :
    print('==') # A와 B가 같을 경우
