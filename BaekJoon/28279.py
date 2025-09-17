# 2025년 7월 7일
# 백준 28279번
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
    my_deck = MyDeck()

    N = int(input())
    
    for _ in range(N) :
        orders = list(map(int, sys.stdin.readline().split()))
        order = orders[0]
        if order == 1 :
            my_deck.push_left(orders[1])
        elif order == 2 :
            my_deck.push_right(orders[1])
        elif order == 3 :
            result = my_deck.pop_left()
            if result == False :
                print(-1)
            else :
                print(result)
        elif order == 4 :
            result = my_deck.pop_right()
            if result == False :
                print(-1)
            else :
                print(result)
        elif order == 5 :
            print(my_deck.get_size())
        elif order == 6 :
            result = my_deck.empty()
            if result == True :
                print(1)
            else :
                print(0)
        elif order == 7 :
            result = my_deck.peek_left()
            if result == False :
                print(-1)
            else :
                print(result)
        elif order == 8 :
            result = my_deck.peek_right()
            if result == False :
                print(-1)
            else :
                print(result)

if __name__ == "__main__" :
    main()