# 2025년 5월 25일 
# 백준 19532번

a, b, c, d, e, f = map(int, input().split(' '))

for x in range(-999, 1000) :
    for y in range(-999, 1000) :
        if (a * x) + (b * y) == c and (d * x) + (e * y) == f :
            print(x, y)
            exit()