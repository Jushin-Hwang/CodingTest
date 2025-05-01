# 2025년 5월 1일
# 백준 2903번

# 1 -> 1번
# 1 + 6 -> 2번
# 1 + 6 + 12 -> 3번
# 1 + 6 + 12 + 18 => 4번 ......

N = int(input())

max_length = 1
count = 1
while max_length < N :
    max_length += (6 * count)
    count += 1

print(count)