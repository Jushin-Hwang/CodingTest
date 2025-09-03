# 2025년 6월 3일 
# 백준 10989번

'''
0902 오답노트 1 : 메모리가 터짐! Counting Sort적용하기!

0903 오답노트 2 : 시간초과가 남!
출력 단계에서 for문 2중 사용하지 말고,
print((str(i) + '\n') * c_array[i], end = '')를 사용해보기로 함!

0903 오답노트 3 : 그래도 시간초과가 남!
import sys 해서
sys.readline()을 해봐야겠음!

0903 오답노트 4 : 시간초과 문제는 해결되었지만, 메모리 초과가 남!
다시 출력 단계에서 2중 for문을 사용해보겠음.
'''
import sys

# N 입력받기
N = int(sys.stdin.readline())

# Counting Array 선언하기
c_array = [0] * 10001

# N개의 줄로부터 입력받아서 해당하는 숫자에 count를 올리기
for _ in range(N) :
    num = int(sys.stdin.readline())
    c_array[num] += 1

# c_array에서 요소를 추출하면서 0이 아닌 경우, 출력하기
for i in range(len(c_array)) :
    if c_array[i] != 0 :
        for j in range(c_array[i]) :
            print(i)