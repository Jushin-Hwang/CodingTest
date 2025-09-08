# 2025년 6월 16일
# 백준 10816번

# Get N input
N = int(input())

# Get card list
card_list = list(map(str, input().split()))

# Make card dictionary
card_dict = dict()
for card in card_list :
    if card in card_dict.keys() :
        card_dict[card] = card_dict[card] + 1
    else :
        card_dict[card] = 1

# Get M input
M = int(input())

# Get check list
check_list = list(map(str, input().split()))

# Check and print the result
for number in check_list :
    if number in card_dict.keys() :
        print(card_dict[number], end = ' ')
    else :
        print('0', end = ' ')

