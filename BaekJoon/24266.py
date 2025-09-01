# 2025년 5월 20일 
# 백준 24266번

'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        for j <- 1 to n
            for k <- 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}
'''

'''
MenOfPassion(A : list, n : int) :
    sum = 0
    for i in range(1, n + 1) :
        for j in range(1, n + 1) :
            for k in range(1, n + 1) :
                sum += A[i] * A[j] * A[k] # 코드 1
    return sum
'''

n = int(input())

count = n ** 3
degree = 3

print(count)
print(degree)
