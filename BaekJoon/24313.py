# 2025년 5월 22일 
# 백준 24313번

a_list = list(input().split(' '))
a0 = int(a_list[0])
a1 = int(a_list[1])

c = int(input())
n0 = int(input())


def cmp(num1, num2, c, n) :
    if (num1 - c) * n + num2 <= 0 :
        return True
    else :
        return False
    
if cmp(a0, a1, c, n0) and cmp(a0, a1, c, 987654321) :
    print(1)
else :
    print(0)