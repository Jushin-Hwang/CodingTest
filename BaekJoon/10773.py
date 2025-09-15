# 2025년 6월 30일
# 백준 10773번
import sys

my_stack = list()

def push(number) :
    my_stack.append(number)

def pop() :
    my_stack.pop()

def main() :
    K = int(input())
    for _ in range(K) :
        num = int(sys.stdin.readline())
        if num == 0 :
            pop()
        else :
            push(num)
    
    sum = 0
    for number in my_stack :
        sum += number

    print(sum)

if __name__ == "__main__" :
    main()