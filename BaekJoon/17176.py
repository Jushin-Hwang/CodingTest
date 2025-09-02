# 2025년 6월 4일 
# 백준 17176번

# 암호문 딕셔너리 저장
my_dict = {' ' : 0,
           '65' : 1,
           '32' : 27}

# N 입력받기
N = int(input())

# 숫자 리스트 입력받기
N_list = []
N_list = list(map(int, input().split(' ')))

N_list.sort()

# 문자열 입력받기
S = input()
S_list = []
for i in range(len(S)) :
    S_list.append(S[i])
S_list.sort()

# S_list를 암호화 하기
for i in range(len(S_list)) :
    if S_list[i] == ' ' :
        S_list[i] = 0
    elif 65 <= ord(S_list[i]) and ord(S_list[i]) < 91 :
        S_list[i] = ord(S_list[i]) - 64
    elif 97 <= ord(S_list[i]) and ord(S_list[i]) < 123 :
        S_list[i] = ord(S_list[i]) - 70

# N_list와 S_list를 비교하기
if N_list == S_list :
    print('y')
else :
    print('n')