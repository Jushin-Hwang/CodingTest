# 2025년 6월 12일
# 백준 10815번

N = int(input())

card_set = set(map(int, input().split()))

M = int(input())

test_list = list(map(int, input().split()))

for num in test_list :
    if num in card_set :
        print(1, end = ' ')
    else :
        print(0, end = ' ')