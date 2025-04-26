# 2025년 4월 26일
# 백준 2753번

def get_number() :
    a = int(input())
    return a

x = get_number() # x값 입력받기
y = get_number() # y값 입력받기

if x > 0 and y > 0 : # 1사분면인 경우
    print(1)
elif x < 0 and y > 0 : # 2사분면인 경우
    print(2)
elif x < 0 and y < 0 : # 3사분면인 경우
    print(3)
elif x > 0 and y < 0 : # 4사분면인 경우
    print(4)
