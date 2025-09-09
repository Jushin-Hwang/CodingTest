# 2025년 6월 18일
# 백준 1269번

N, M = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))

a = len(A - B)
b = len(B - A)

print(a + b)