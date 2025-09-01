# 2025년 5월 26일 
# 백준 1018번

# define answer
max_n = 987654321

# Templates
line_1 = 'WBWBWBWB'
line_2 = 'BWBWBWBW'

# Get N, M
N, M = map(int, input().split(' '))

# Draw whole board
my_map = []
for i in range(N) :
    my_map.append(input())

# Count Different Tiles
def count_diff(type, my_map) :
    count = 0
    for i in range(8) :
        if type == 0 :
            if i % 2 == 0 :
                line = line_1
            else :
                line = line_2
        elif type == 1 :
            if i % 2 == 0 :
                line = line_2
            else :
                line = line_1
        my_line = my_map[i]
        for j in range(8) :
            if line[j] != my_line[j] :
                count += 1
    return count

i = 0
while(i < N - 7) :
    for j in range(0, M - 7) :
        cutted_map = []
        for k in range(i, i + 8) :
            cutted_line = my_map[k][j : j + 8]
            cutted_map.append(cutted_line)
        new_count = min(count_diff(0, cutted_map), count_diff(1, cutted_map))
        if new_count < max_n :
            max_n = new_count
    i += 1

print(max_n)

