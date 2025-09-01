# 2025년 5월 27일 
# 백준 1436번
# 다른 방법으로 풀어보기

# Get N
N = int(input())

# initialize vars
num = 666
count = 0

# main code
while(1) :
    if '666' in str(num) :
        count += 1
        if count == N :
            print(num)
            break
    num += 1