# 2024년 9월 5일 
# 백준 2908번

A, B = input().split()

n1, n2 = int(A[0]), int(A[2])
n3, n4 = int(B[0]), int(B[2])

A = int(A)
B = int(B)

A = A - (n1 * 100) - n2 + n1 + (n2*100)
B = B - (n3 * 100) - n4 + n3 + (n4*100)

print(max(A, B))