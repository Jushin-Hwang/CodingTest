# 2025년 5월 7일
# 백준 25206번

N = int(input())
i = 2

if N == 1 :
    print('')
    exit()
else :
    while(i < N) :
        if N % i == 0 :
            print(i)
            N = N / i
            i = 2
            continue
        else :
            i += 1

print(int(N))