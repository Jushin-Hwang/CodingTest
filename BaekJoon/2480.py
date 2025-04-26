# 2025년 4월 26일
# 백준 2480번

def get_numbers() :
    a = [int(number) for number in input().split(' ')]
    return a

def how_many_dice_num(dices, number) :
    count = 0
    for dice in dices :
        if dice == number :
            count += 1
    return count

dices = get_numbers() # 숫자 2개 리스트로 입력받기

result_howmany = [] # 같은 숫자가 몇개 있는지 저장하는 list
for dice in dices :
    howmany = how_many_dice_num(dices, dice) # 같은 숫자가 몇개 나왔는지 확인하는 함수
    result_howmany.append(howmany) # return값 list에 저장

if max(result_howmany) == 3 : # 3개의 주사위가 같은 숫자가 나올 경우
    number = dices[0]
    prize = 10000 + 1000 * number
elif max(result_howmany) == 2 :
    number = dices[result_howmany.index(2)] # 2개의 주사위가 같은 숫자가 나올 경우
    prize = 1000 + 100 * number 
elif max(result_howmany) == 1 : # 모든 주사위가 다른 숫자일 경우
    number = max(dices)
    prize = 100 * number

print(prize) # 결과 출력