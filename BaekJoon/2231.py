# 2025년 5월 24일 
# 백준 2231번

N = int(input())

def solution() :
    t_list = []
    for test in range(N) :
        sum = temp = test
        while(temp != 0) :
            t_list.append(temp % 10)
            temp = temp // 10
        for n in range(len(t_list)) :
            sum += t_list[n]
        if sum == N :
            print(test)
            return
        t_list = []
    print(0)
    return
        
solution()

        