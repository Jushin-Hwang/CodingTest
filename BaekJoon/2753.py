# 2025년 4월 26일
# 백준 2753번

def get_number() :
    a = int(input())
    return a

def is_leap_year(year) :
    if year % 4 == 0 : # year가 4의 배수이고
        if year % 100 != 0 or year % 400 == 0 : # year가 100의 배수가 아니거나, 400의 배수인 경우
            return 1 # year는 윤년, 1 return
        else :
            return 0 # 그렇지 않다면 year는 윤년이 아님, 0 return
    else :
        return 0 # 그렇지 않다면 year는 윤년이 아님, 0 return

year = get_number() # 숫자 입력받기

print(is_leap_year(year)) # 윤년인지 확인한 return값 출력
