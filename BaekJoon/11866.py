# 2025년 7월 6일
# 백준 11866번

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
        
def print_result(result : list) :
    print('<', end = '')
    for i in range(len(result) - 1) :
        print(result[i], end = ', ')
    print(f"{result[-1]}>")

    
def main() :
    my_queue = MyQueue()
    
    N, K = map(int, input().split())
    for i in range(1, N + 1) :
        my_queue.push(i)

    counter = 0
    result = list()

    while(not my_queue.empty()) :
        counter += 1
        target = my_queue.pop()
        if counter % K == 0 :
            result.append(target)
        else :
            my_queue.push(target)

    print_result(result)
        
if __name__ == "__main__" :
    main()