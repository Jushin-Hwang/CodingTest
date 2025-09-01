# 2025년 5월 27일 
# 백준 1436번

# Get N
N = int(input())

def check_devilnumber(number) :
    check_string = str(number)
    for i in range(len(check_string) - 2) :
        if check_string[i] == '6' and check_string[i + 1] == '6' and check_string[i + 2] == '6' :
            return True

num = 666
count = 0
while(1) :
    if check_devilnumber(num) :
        count += 1
        if count == N :
            print(num)
            break
    num += 1