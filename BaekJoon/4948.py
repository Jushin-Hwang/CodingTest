# 2025년 6월 26일
# 백준 4948번

'''
시간초과 문제 발생..! 그러나 코드 자체 흐름은 나쁘지 않아서 이대로 저장해도 좋을 것 같음!
'''
import sys
import math

def is_prime(number) :
    if number == 1 :
        return False
    elif number == 2 :
        return True
    
    for i in range(2, int(math.sqrt(number) + 1)) :
        if number % i == 0 :
            return False
        
    return True

def solution(start) :
    end = 2 * start
    pt = start + 1
    cnt = 0

    while(pt <= end) :
        if is_prime(pt) :
            cnt += 1

        pt += 1
    
    return cnt

def main() :
    while(True) :
        num = int(sys.stdin.readline())
        if num == 0 :
            return
        else :
            ans = solution(num)
            print(ans)

if __name__ == '__main__' :
    main()