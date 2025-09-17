# 2025년 7월 4일
# 백준 18258번

import sys

class MYQUEUE :   
    def __init__(self):
        self.pt = -1
        self.queue = list()
    
    def push(self, number) :
        self.queue.append(number)
    
    def pop(self) :
        if self.empty() :
            return -1
        else :
            self.pt += 1
            return self.queue[self.pt]

    def size(self) :
        return len(self.queue) - (self.pt + 1)

    def empty(self) :
        if self.size() == 0 :
            return 1
        else :
            return 0

    def front(self) :
        if self.empty() :
            return -1
        else :
            return self.queue[self.pt + 1]

    def back(self) :
        if self.empty() :
            return -1
        else :
            return self.queue[-1]

def main() :
    my_queue = MYQUEUE()
    N = int(input())
    for _ in range(N) :
        orders = list(map(str, sys.stdin.readline().split()))
        if orders[0] == "push" :
            my_queue.push(orders[1])
        elif orders[0] == 'pop' :
            print(my_queue.pop())
        elif orders[0] == 'size' :
            print(my_queue.size())
        elif orders[0] == 'empty' :
            print(my_queue.empty())
        elif orders[0] == 'front' :
            print(my_queue.front())
        elif orders[0] == 'back' :
            print(my_queue.back())          

if __name__ == "__main__" :
    main()