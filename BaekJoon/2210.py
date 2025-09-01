# 2025년 5월 30일 
# 백준 2210번

# making number tree
def get_sum(map, x, y, count, num_list = [None, None, None, None, None, None]) :
    global results
    num_list[count] = (map[x][y])
    if count == 5 :
        sum = num_list[0] * 100000
        sum += num_list[1] * 10000
        sum += num_list[2] * 1000
        sum += num_list[3] * 100
        sum += num_list[4] * 10
        sum += num_list[5] * 1
        results.add(sum)
        return
    else :
        count += 1
        if 0 < x :
            next_x = x - 1
            get_sum(map, next_x, y, count, num_list)
        if x < 4 :
            next_x = x + 1
            get_sum(map, next_x, y, count, num_list) 
        if 0 < y :
            next_y = y - 1
            get_sum(map, x, next_y, count, num_list)
        if y < 4 :
            next_y = y + 1
            get_sum(map, x, next_y, count, num_list)

# Initialize Vars
results = set()

# Initialize Map
my_map = [[0 for _ in range(5)] for __ in range(5)]

# Get Inputs
for i in range(5) :
    my_map[i] = list(map(int, input().split(' ')))

for y in range(5) :
    for x in range(5) :
        get_sum(my_map, x, y, 0)

print(len(results))