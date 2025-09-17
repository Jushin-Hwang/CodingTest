# 2025년 7월 5일
# 백준 2164번

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
    N = int(input())
    numbers = MYQUEUE()
    for i in range(N) :
        numbers.push(i + 1)

    while(not numbers.empty()) :
        for __ in range(2) :
            num = numbers.pop()
            if numbers.empty() :
                print(num)
                return
        numbers.push(num)


if __name__ == "__main__" :
    main()