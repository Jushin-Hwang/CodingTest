# 2025년 6월 29일
# 백준 28278번
import sys

my_stack = list()

def push(number) :
    my_stack.append(number)

def pop() :
    try :
        print(my_stack.pop())
    except :
        print(-1)

def get_len() :
    print(len(my_stack))    

def is_empty() :
    if len(my_stack) == 0 :
        print(1)
    else :
        print(0)

def peek() :
    try :
        print(my_stack[-1])
    except :
        print(-1)

def main() :
    N = int(input())
    
    for _ in range(N) :
        order = list(map(int, sys.stdin.readline().split()))
        if order[0] == 1 :
            push(order[1])
        elif order[0] == 2 :
            pop()
        elif order[0] == 3 :
            get_len()
        elif order[0] == 4 :
            is_empty()
        elif order[0] == 5 :
            peek()

if __name__ == "__main__" :
    main()