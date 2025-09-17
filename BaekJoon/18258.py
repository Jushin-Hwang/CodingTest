# 2025년 7월 4일
# 백준 18258번

import sys

class MYQUEUE :
    queue = list()
    
    def push(self, number) :
        self.queue.append(number)
    
    def pop(self) :
        if len(self.queue) == 0 :
            print(-1)
        else :
            print(self.queue.pop(0))
    
    def size(self) :
        print(len(self.queue))

    def empty(self) :
        if len(self.queue) == 0 :
            print(1)
        else :
            print(0)

    def front(self) :
        if len(self.queue) == 0 :
            print(-1)
        else :
            print(self.queue[0])

    def back(self) :
        if len(self.queue) == 0 :
            print(-1)
        else :
            print(self.queue[-1])  

def main() :
    my_queue = MYQUEUE()
    N = int(input())
    for _ in range(N) :
        orders = list(map(str, sys.stdin.readline().split()))
        if orders[0] == "push" :
            my_queue.push(orders[1])
        elif orders[0] == 'pop' :
            my_queue.pop()
        elif orders[0] == 'size' :
            my_queue.size()
        elif orders[0] == 'empty' :
            my_queue.empty()
        elif orders[0] == 'front' :
            my_queue.front()
        elif orders[0] == 'back' :
            my_queue.back()
            

if __name__ == "__main__" :
    main()