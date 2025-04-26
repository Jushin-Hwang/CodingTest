# 2025년 4월 26일
# 백준 2558번

num1 = int(input()) # (1) 숫자 받기
num2 = int(input()) # (2) 숫자 받기

num2_h = num2 // 100 # (2) 숫자의 100의자리 숫자
num2_t = (num2 % 100) // 10  # (2) 숫자의 10의자리 숫자
num2_o = (num2 % 10) # (2) 숫자의 1의자리 숫자

print(num1 * num2_o) # (3) 숫자 출력
print(num1 * num2_t) # (4) 숫자 출력
print(num1 * num2_h) # (5) 숫자 출력
print(num1 * num2) # (6) 숫자 출력
