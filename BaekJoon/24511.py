# 2025년 7월 9일
# 백준 24511번
class MyQueue :
    class Node :
        def __init__(self, value = None) :
            self.value = value
            self.front = None
            self.rear = None

        def set_front(self, front_node) :
            self.front = front_node

        def set_rear(self, rear_node) :
            self.rear = rear_node

    def __init__(self) :
        self.root_node = None
        self.f_point = self.root_node
        self.r_point = self.root_node

    def push(self, value) :
        new_node = self.Node(value = value)
        if self.root_node == None : 
            self.root_node = new_node
            self.f_point = self.root_node
            self.r_point = self.root_node
        else : 
            new_node.set_front(self.r_point)
            self.r_point.set_rear(new_node)
            self.r_point = new_node
        
    def pop(self) :
        if self.empty() :
            return None
        else : 
            popped_node = self.f_point
            self.root_node = self.f_point = self.f_point.rear
            return popped_node.value
    
    def size(self) :
        if self.empty() :
            return 0
        cnt = 1
        pointer = self.f_point
        while(True) :
            if pointer == self.r_point :
                return cnt
            else :
                pointer = pointer.rear
                cnt += 1

    def empty(self) :
        if self.f_point == None :
            return True
        else : 
            return False

def main() :
    my_queue = MyQueue()
    N = int(input())
    queuestack_list = list(map(int, input().split()))
    item_list = list(map(int, input().split()))
    for i in range(len(queuestack_list) - 1, -1, -1) :
        if queuestack_list[i] == 0 :
            my_queue.push(item_list[i])

    M = int(input())
    C = list(map(int, input().split()))

    result = list()
    for i in range(M) :
        my_queue.push(C[i])
        result.append(my_queue.pop())
    
    for ans in result :
        print(ans, end = ' ')

if __name__ == "__main__" :
    main()