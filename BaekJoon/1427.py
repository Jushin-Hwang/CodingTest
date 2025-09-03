# 2025년 6월 5일
# 백준 1427번

# 숫자를 저장할 빈 리스트 선언
n_array = []

# 숫자를 문자열 형태로 입력
inputs = input()

# 각 문자를 리스트에 추가
for number in inputs :
    n_array.append(number)

# 리스트의 요소를 내림차순으로 정렬
n_array.sort(reverse = True)

# 각 요소를 한 줄에 이어서 출력
for number in n_array :
    print(number, end = '')
    