# 2025년 6월 27일
# 백준 17103번
import sys

n_max = 1000000

prime_list = [True] * (n_max + 1)

prime_list[1] = False

for i in range(2, n_max) :
    if prime_list[i] == True :
        multiple = 2
        while(i * multiple <= n_max) :
            prime_list[i * multiple] = False
            multiple += 1

def solution(number) :
    cnt = 0
    for i in range(1, (number // 2) + 1) :
        if prime_list[i] == True and prime_list[number - i] == True :
            cnt += 1
    return cnt

def main() :
    T = int(input())
    for _ in range(T) :
        N = int(sys.stdin.readline())
        print(solution(N))

if __name__ == '__main__' :
    main()