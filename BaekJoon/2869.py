# 2025년 5월 1일
# 백준 2869번

line = input().split(' ')

A = int(line[0])
B = int(line[1])
V = int(line[2])

day = 1
height = 0
distance = A - B

if (V - A) % distance == 0 :
    day = (V - A) // distance + 1
else :
    day = (V - A) // distance + 2

print(day)