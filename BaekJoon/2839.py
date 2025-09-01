# 2025년 5월 28일 
# 백준 2839번

# Get N
N = int(input())

# Get the maximum number of 5kg bags.
max_5kg = N // 5

# Main code
for paperbag_5kg in range(max_5kg, -1, -1) :
    weight = paperbag_5kg * 5
    paperbag_3kg = 0
    while(1) :
        if weight < N :
            weight += 3
            paperbag_3kg += 1
        elif weight == N :
            print(paperbag_5kg + paperbag_3kg)
            exit()
        else :
            break
print(-1)