# 2025년 4월 26일
# 백준 8393번

def get_number() :
    a = int(input())
    return a

n = get_number() # n 입력받기
sum = 0 # sum값 초기화
for i in range(n + 1) : # 1부터 n까지의 합 구하기
    sum += i 
print(sum) # 결과 출력