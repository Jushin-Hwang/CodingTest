# 2025년 7월 8일
# 백준 2346번
import sys

class MyDeck :
    class Node :
        def __init__(self) :
            self.value = None
            self.front = None
            self.rear = None

        def set_value(self, value) :
            self.value = value

        def set_front(self, front_node) :
            self.front = front_node

        def set_rear(self, rear_node) :
            self.rear = rear_node

        def get_value(self) :
            return self.value

        def get_front(self) :
            return self.front
        
        def get_rear(self) :
            return self.rear
        
    def __init__(self) :
        self.f_point = None
        self.r_point = None
        self.size = 0

    def push_left(self, value) :
        new_node = self.Node()
        new_node.set_value(value)
        self.size += 1

        if self.f_point == None : 
            self.f_point = new_node
            self.r_point = new_node
        else :
            new_node.set_rear(self.f_point)
            self.f_point.set_front(new_node)
            self.f_point = new_node

    def push_right(self, value) :
        new_node = self.Node()
        new_node.set_value(value)
        self.size += 1

        if self.r_point == None : 
            self.f_point = new_node
            self.r_point = new_node
        else :
            new_node.set_front(self.r_point)
            self.r_point.set_rear(new_node)
            self.r_point = new_node

    def pop_left(self) :
        if self.empty() :
            return False
        else :
            self.size -= 1
            popped_node = self.f_point
            self.f_point = popped_node.get_rear()
            if self.f_point == None :
                self.r_point = None
            else :
                self.f_point.set_front(None)
            return popped_node.get_value()
        
    def pop_right(self) :
        if self.empty() :
            return False
        else :
            self.size -= 1
            popped_node = self.r_point
            self.r_point = popped_node.get_front()
            if self.r_point == None :
                self.f_point = None
            else :
                self.r_point.set_rear(None)
            return popped_node.get_value()
        
    def get_size(self) :
        return self.size
    
    def empty(self) :
        if self.get_size() == 0 :
            return True
        else :
            return False

    def peek_left(self) :
        if self.empty() :
            return False
        else :
            return self.f_point.get_value()
    
    def peek_right(self) :
        if self.empty() :
            return False
        else :
            return self.r_point.get_value()
        
def main() :
    N = int(input())
    balloons = list(map(int, input().split()))
    my_deck = MyDeck()
    for i in range(len(balloons)) :
        my_deck.push_right([i + 1, balloons[i]])

    result = list()
    while(True) :
        next = my_deck.pop_left()
        result.append(next[0])
        if my_deck.empty() :
            break
        if next[1] > 0 :
            for _ in range(next[1] - 1) :
                my_deck.push_right(my_deck.pop_left())
        elif next[1] < 0 :
            for _ in range(-next[1]) :
                my_deck.push_left(my_deck.pop_right())

    for item in result :
        print(item, end = ' ')

if __name__ == "__main__" :
    main()