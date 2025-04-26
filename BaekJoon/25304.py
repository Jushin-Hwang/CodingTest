# 2025년 4월 26일
# 백준 25304번

def get_number() :
    a = int(input())
    return a

def get_numbers() :
    a = [int(number) for number in input().split(' ')]
    return a

X = get_number() # 영수증에 적힌 총 금액
N = get_number() # 구매한 물건의 종류의 수
sum = 0 # sum값 초기화
for i in range(N) : # 구매한 물건의 종류의 수만큼 반복
    shop_list = get_numbers()
    price = shop_list[0] # 각 물건의 가격
    howmany = shop_list[1] # 각 물건의 갯수
    sum += price * howmany # sum값 계산

if sum == X : # 영수증에 적힌 총 금액과 계산한 sum값이 일치하는 경우
    print("Yes")
else : # 그렇지 않은 경우
    print("No")