# 2025년 5월 21일 
# 백준 24267번

'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 2
        for j <- i + 1 to n - 1
            for k <- j + 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}
'''

'''
MenOfPassion(A : list, n : int) {
    sum = 0
    for i in range(1, n - 1) :
        for j in range(i + 1, n) :
            for k in range(j + 1, n + 1) :
                sum = sum + (A[i] * A[j] * A[k]) # 코드 1
}
'''

def fiv(number) :
    if number % 2 == 0 :
        share = number // 2
        return share * (number + 1)
    else :
        share = number // 2
        return (share * number) + number

def count(number) :
    count = 0
    for i in range(number + 1) :
        if i >= 3 :
            count += fiv(i - 2)

    return count

n = int(input())

print(count(n))
print(3)