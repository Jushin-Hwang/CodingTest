# 2025년 7월 3일
# 백준 12789번

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
    N = int(input())
    lines = list(map(int, input().split()))
    cnt = 1
    line_stack = list()
    while(cnt <= N) :
        if peek(line_stack) == cnt :
            pop(line_stack)
            cnt += 1
        else :
            try :
                new_ticket = lines.pop(0)
                if new_ticket == cnt :
                    cnt += 1
                else :
                    push(new_ticket, line_stack)
            except :
                print('Sad')
                return
    print("Nice")
    return
            

if __name__ == "__main__" :
    main()