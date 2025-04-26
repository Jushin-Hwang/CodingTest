# 2025년 4월 26일
# 백준 25314번

def get_number() :
    a = int(input())
    return a

N = get_number() # 정수 N 입력

howmany_long = N // 4 # 얼마나 long을 붙일지 계산
result = "" # result 초기화
for i in range(howmany_long) :
    result += "long " # long의 갯수만큼 result에 append

result += "int" # 마지막은 int로 끝남

print(result) # 결과 출력