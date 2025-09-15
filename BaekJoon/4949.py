# 2025년 7월 2일
# 백준 4949번
import sys

def push(number, my_stack) :
    my_stack.append(number)

def pop(my_stack) :
    my_stack.pop()

def peek(my_stack) :
    try :
        return my_stack[-1]
    except :
        return False

def is_empty(my_stack) :
    if len(my_stack) == 0 :
        return True
    else :
        return False

def init_stacks() :
    my_stack = list()
    return my_stack
    

def main() :
    while(True) :
        line = input()
        if line == '.' :
            return

        m_stack = init_stacks()
        flag = False
        for char in line :
            if char == "(" :
                push('Small', m_stack)
            elif char == ')' :
                if peek(m_stack) == 'Small' :
                    pop(m_stack)
                else :
                    print('no')
                    flag = True
                    break
            elif char == "[" :
                push('Big', m_stack)
            elif char == ']' :
                if peek(m_stack) == "Big" :
                    pop(m_stack)
                else :
                    print('no')
                    flag = True
                    break

        if flag == False :
            if is_empty(m_stack) :
                print("yes")
            else :
                print("no")

if __name__ == "__main__" :
    main()