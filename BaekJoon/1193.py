# 2025년 5월 1일
# 백준 1193번

def get_level(number) :
    count = 0
    max_level = 0
    while max_level < number :
        count += 1
        max_level += count
    return count, max_level

# i + j = level
# max_level - level < number <= max_level
# max_level에서는 j == 1, i == level - j

X = int(input())
level, max_level = get_level(X)
initial_level = max_level - level + 1
if level % 2 == 0 :
    i = 1
    j = level - i + 1
    while(initial_level != X) :
        initial_level += 1
        i += 1
        j -= 1
else :
    j = 1
    i = level - j + 1
    while(initial_level != X) :
        initial_level += 1
        i -= 1
        j += 1

print(f"{i}/{j}")