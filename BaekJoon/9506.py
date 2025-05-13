# 2025년 5월 4일
# 백준 9506번

while(True) :
    factors = []
    sum = 0
    result = ''
    num = int(input())
    if num == -1 :
        break
    for i in range(1, num) :
        if num % i == 0 :
            factors.append(i)
    for factor in factors :
        sum += factor
    if sum == num :
        result += f"{num} = "
        for factor in factors :
            result += f"{factor} + "
        print(result[:-2])
    else :
        print(f"{num} is NOT perfect.")
    
        
