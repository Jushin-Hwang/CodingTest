# 2025년 6월 9일
# 백준 1181번

len_list = [[] for _ in range(51)]

# N 입력받기
N = int(input())

# 단어 리스트에 단어 추가하기

for i in range(N) :
    word = input()
    len_list[len(word)].append(word)

# 단어 정렬하기
res = []
for word_list in len_list :
    word_list = list(set(word_list))
    word_list.sort()
    res.extend(word_list)

# 결과 출력하기
for i in range(len(res)) :
    print(res[i])