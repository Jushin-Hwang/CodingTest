# 2025년 6월 15일
# 백준 1620번
'''
0908 오답노트 1 : 시간초과 발생!
sys.stdin.readline()을 사용해서 시간을 줄여 해결함

0908 오답노트 2 : 출력 형식 문제 발생!
한번에 여러 줄을 입력했을 때, 이유는 모르겠지만 print로는 마지막에 해당하는 결과만 출력됨.
result 리스트를 만들어 result에 저장 후 출력하는 방법으로 문제를 해결함.

0908 추가 : try ~ except문을 사용했는데, 그러지 말고 isdigit()함수를 사용하는게 가독성이 더 좋음!'''
import sys

N, M = map(int, input().split())

pokedex = dict()
for i in range(N) :
    name = sys.stdin.readline().strip()
    pokedex[i+1] = name
    pokedex[name] = i+1

result = []
for _ in range(M) :
    quest = sys.stdin.readline().strip()

    if quest.isdigit() :
        result.append(pokedex[int(quest)])
    else :
        result.append(pokedex[quest])

for ans in result :
    print(ans)