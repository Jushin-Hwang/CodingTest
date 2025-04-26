# 2025년 4월 26일
# 백준 2884번

def get_numbers() :
    a = [int(number) for number in input().split(' ')]
    return a

Time_list = get_numbers() # 숫자 2개 리스트로 입력받기
H = Time_list[0] # H 추출하기
M = Time_list[1] # M 추출하기

setting_H = H
setting_M = M - 45 # 세팅 시간 바꿔주기
if setting_M < 0 : # 분이 음수일 경우, 시가 1 줄고, 분이 60 늘어남
    setting_H -= 1
    setting_M += 60
if setting_H < 0 : # 시가 음수일 경우, 시가 24 늘어남 (전날)
    setting_H += 24

print(f"{setting_H} {setting_M}") # 결과 출력