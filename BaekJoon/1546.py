# 2025년 4월 26일
# 백준 1546번
import sys

def get_number() :
    a = sys.stdin.readline().rstrip()
    a_int = int(a)
    return a_int

def get_numbers() :
    a = sys.stdin.readline().rstrip()
    a_list = [int(number) for number in a.split(' ')]    
    return a_list

N = get_number() # N 입력받기
if N > 0 :
    score_list = get_numbers() # 점수 list 입력받기

max_score = max(score_list) # max값 구하기

new_score_list = []
for score in score_list :
    new_score = score/max_score*100
    new_score_list.append(new_score) # 새로운 성적 계산해서 저장하기

sum = 0
for new_score in new_score_list :
    sum += new_score 
average = sum / N # 새로운 성적 average값 계산하기

print(average) # 결과 출력하기