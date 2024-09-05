# 2024년 9월 5일 
# 백준 2908번
# 응용 1 : [::-1] 을 사용해보자.

A, B = input().split()

A, B = int(A[::-1]), int(B[::-1])

print(max(A, B))