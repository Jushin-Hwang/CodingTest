# 2025년 7월 1일
# 백준 9012번
import sys

my_stack = list()

def push(number) :
    my_stack.append(number)

def pop() :
    my_stack.pop()

def is_empty() :
    if len(my_stack) == 0 :
        return True
    else :
        return False

def init() :
    global my_stack
    my_stack = []
    

def main() :
    
    N = int(input())
    for _ in range(N) :
        init()
        flag = False
        line = sys.stdin.readline()
        for char in line :
            if char == "(" :
                push('Dummy')
            elif char == ')' :
                if is_empty() :
                    print('NO')
                    flag = True
                    break
                else :
                    pop()

        if flag == False :
            if is_empty() :
                print("YES")
            else :
                print("NO")

if __name__ == "__main__" :
    main()