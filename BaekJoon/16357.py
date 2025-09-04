# 2025년 6월 8일
# 백준 16357번

'''
[[A번 식물, 광합성, 운동성]]
광합성이 1이고, 운동성이 0이면 식물
=> 광합성이 0이면 식물 X
=> 운동성이 1이면 식물 X
'''

# 함수 구현
def get_min(p_list) :
    cnt = 0
    for plant in p_list :
        if plant[1] == 1 and plant[2] == 0 :
            cnt += 1

    return cnt

def get_max(p_list) :
    cnt = 0
    for plant in p_list :
        if plant[1] != 0 and plant[2] != 1 :
            cnt += 1

    return cnt

# main code
N, M = map(int, input().split(' '))
plant_list = [[i, -1, -1] for i in range(N)]

for _ in range(M) :
    exp = list(map(str, input().split(' ')))
    a = int(exp[0])
    b = exp[1]
    result = int(exp[2])

    if b == 'P' :
        if result == 0 :
            plant_list[a - 1][1] = 0
        elif result == 1 :
            plant_list[a - 1][1] = 1
    elif b == 'M' :
        if result == 0 :
            plant_list[a - 1][2] = 0
        elif result == 1 :
            plant_list[a - 1][2] = 1

min_num = get_min(plant_list)
max_num = get_max(plant_list)

print(min_num, max_num)