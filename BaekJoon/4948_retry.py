# 2025년 6월 26일
# 백준 4948번 수정 1 : 에라토스테네스의 체 활용
import sys

n_max = 123456 * 2

prime_list = [True] * (n_max + 1)

prime_list[1] = False
for i in range(2, n_max) :
    if prime_list[i] == True :
        multiple = 2
        while(i * multiple <= n_max) :
            prime_list[i * multiple] = False
            multiple += 1

def solution(start) :
    end = start * 2
    cnt = 0
    for i in range(start + 1, end + 1) :
        if prime_list[i] == True :
            cnt += 1

    return cnt

def main() :
    while(True) :
        number = int(sys.stdin.readline())
        if number == 0 :
            return
        print(solution(number))

if __name__ == '__main__' :
    main()
