# 2025년 6월 23일
# 백준 2485번
import sys

N = int(input())

def GCD(a, b) :
    if a == b :
        return a
    elif a == 0 :
        return b
    elif b == 0 :
        return a
    
    if a < b :
        return GCD(a, b % a)
    else :
        return GCD(b, a % b)
    
tree_location = list()
for i in range(N) :
    number = int(sys.stdin.readline())
    
    if i == 0 :
        root_number = number
    
    tree_location.append(number - root_number)

gcd = 0
for i in range(N) :
    gcd = GCD(gcd, tree_location[i])

total_tree_cnt = (tree_location[-1] // gcd) + 1
current_tree_cnt = len(tree_location)

print(total_tree_cnt - current_tree_cnt)