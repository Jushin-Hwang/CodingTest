# 2025년 4월 27일
# 백준 11720번

N = int(input()) # N값 입력받기
if N > 0 :
    numbers_string = input() # numbers_string값 입력받기
    numbers_list = list(numbers_string) # numbers_string을 list형태로 변환

    sum = 0
    for number in numbers_list :
        sum += int(number) # numbers_list에서 요소를 뽑아 정수형으로 변환 후 sum에 추가

    print(sum) # sum값 출력