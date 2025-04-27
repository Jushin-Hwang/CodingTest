# 2025년 4월 26일
# 백준 5597번
import sys

def get_number() :
    a = sys.stdin.readline().rstrip()
    a_int = int(a)
    return a_int

attendance_list = [i + 1 for i in range(30)] # 1부터 30까지의 값 저장
for i in range(28) :
    attendance = get_number() # 숫자 입력받기
    attendance_list.remove(attendance) # list에서 값 제거

for bad_student in attendance_list :
    print(bad_student) # 결과 출력