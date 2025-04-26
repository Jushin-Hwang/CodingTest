# 2025년 4월 26일
# 백준 9498번

def get_number() :
    a = int(input())
    return a

score = get_number() # 숫자 입력받기

if score <= 100 and score >= 90 :
    print('A') # 성적이 A인 경우
elif score >= 80 :
    print('B') # 성적이 B인 경우
elif score >= 70 :
    print('C') # 성적이 C인 경우
elif score >= 60 :
    print('D') # 성적이 D인 경우
else :
    print('F') # 성적이 F인 경우
