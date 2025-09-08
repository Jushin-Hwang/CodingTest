# 2025년 6월 14일
# 백준 7785번

'''
0908 오답노트 1 : 시간초과 발생!
기존 list 형태로 선언되었던 c_members를 set형식으로 변환

0908 오답노트 2 : list(c_members).sort(reverse = True)는 적합하지 않은 문장
c_members_list = list(c_memvers) 하고
c_members_list.sort(reverse = True)해서 항상 내림차순으로 정렬될 수 있도록 문장을 수정
'''

N = int(input())

c_members = set()
for _ in range(N) :
    name, log = input().split(' ')
    if log == "enter" :
        c_members.add(name)
    elif log == "leave" :
        c_members.remove(name)

c_members_list = list(c_members)
c_members_list.sort(reverse = True)

for member in c_members_list :
    print(member)