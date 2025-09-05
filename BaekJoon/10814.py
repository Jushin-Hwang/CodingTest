# 2025년 6월 10일
# 백준 10814번

# N 입력받기
N = int(input())

# N만큼 회원정보 입력받기
member_list = []
for _ in range(N) :
    age, name = map(str, input().split())
    age = int(age)
    member_list.append([age, name])

member_list.sort(key = lambda member : member[0])

for member in member_list :
    print(member[0], member[1])