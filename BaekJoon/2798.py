# 2025년 5월 23일 
# 백준 2798번

N, M = input().split(' ')
N = int(N)
M = int(M)
num_list = list(input().split(' '))
for i in range(len(num_list)) :
    num_list[i] = int(num_list[i])
result = []

def solution() :
    for i in range(0, N-2) :
        for j in range(i + 1, N-1) :
            for k in range(j + 1, N) :
                diff = M - (num_list[i] + num_list[j] + num_list[k])
                if diff >= 0 :
                    result.append(diff)

    print(M - min(result))

solution()