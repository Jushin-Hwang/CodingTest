# 2025년 5월 2일
# 백준 5086번

def get_numbers() :
    a, b = input().split(' ')
    a = int(a)
    b = int(b)
    return a, b

def is_factor(num1, num2) :
    if num2 % num1 == 0 :
        return 1
    else :
        return 0

def is_multiple(num1, num2) :
    if num1 % num2 == 0 :
        return 1
    else :
        return 0

def solution(a, b) :
    if is_factor(a, b) :
        return "factor"
    elif is_multiple(a, b) :
        return "multiple"
    else :
        return "neither"

a, b = get_numbers()
while(a != 0 or b != 0) :
    result = solution(a, b)
    print(result)
    a, b = get_numbers()