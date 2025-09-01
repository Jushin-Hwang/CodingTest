# 2025년 5월 19일 
# 백준 24265번

'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 1
        for j <- i + 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}
'''

'''
MenOfPassion(A : list, n : int) :
    sum = 0
    for i in range(1, n) :
        for j in range(i + 1, n + 1) :
            sum += A[i] * A[j]
    return sum
'''

n = int(input())

count = 0
for i in range(n) :
    count += i

degree = 2

print(count)
print(degree)
