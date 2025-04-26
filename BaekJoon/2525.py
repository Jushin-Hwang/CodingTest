# 2025년 4월 26일
# 백준 2525번

def get_numbers() :
    a = [int(number) for number in input().split(' ')]
    return a

def get_number() :
    a = int(input())
    return a

Time_list = get_numbers() # 숫자 2개 리스트로 입력받기
A = Time_list[0] # A 추출하기
B = Time_list[1] # B 추출하기
C = get_number() # C 입력받기

setting_H = A
setting_M = B + C # 세팅 시간 바꿔주기
while(setting_M >= 60) : # 분이 60보다 클 경우(시가 늘어날 경우), 시가 1 늘고, 분이 60 줄어듬
    setting_H += 1
    setting_M -= 60
while(setting_H >= 24) : # 시가 24보다 클 경우(날짜가 바뀔 경우), 시가 24 줄어듬 (다음날)
    setting_H -= 24

print(f"{setting_H} {setting_M}") # 결과 출력