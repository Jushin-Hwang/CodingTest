# 2025년 5월 31일 
# 백준 2587번

num_list = []
for _ in range(5) :
    num_list.append(int(input()))

num_list.sort()

print(sum(num_list) // len(num_list))
print(num_list[2])