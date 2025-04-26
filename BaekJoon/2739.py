# 2025년 4월 26일
# 백준 2739번

def get_number() :
    a = int(input())
    return a

number = get_number() # 숫자 입력받기

for i in range(9) : # 9단까지 9번 반복
    print(f"{number} * {i + 1} = {number * (i + 1)}") # 결과 출력