# 2025년 4월 28일
# 백준 2444번

N = int(input())

for i in range(N) :
    print(' ' * (N - i - 1), end = '')
    print('*' * (2 * i + 1))

for i in range(N - 1) :
    print(' ' * (i + 1), end = '')
    print('*' * (2 * (N - 1 - i) - 1))