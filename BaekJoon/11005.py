# 2025년 5월 1일
# 백준 11005번

line = input().split(' ')
number = int(line[0])
b = int(line[1])

def get_max_digit(number) :
    max_digit = 0
    while True :
        number = number // b
        if number > 0 :
            max_digit += 1
        else :
            break
    return max_digit

max_digit = get_max_digit(number)
number_list = []
while max_digit != 0 :
    divisor = b ** max_digit
    share = number // divisor
    number_list.append(share)
    number = number % divisor
    max_digit -= 1
number_list.append(number)

for number in number_list :
    if number < 10 :
        print(str(number), end = '')
    else :
        print(chr(number + 55), end = '')