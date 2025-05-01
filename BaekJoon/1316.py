# 2025년 5월 1일
# 백준 1316번

def solution() :
    word = input()
    word_list = []
    for letter in word :
        if letter in word_list :
            if letter is word_list[-1] :
                continue
            else :
                return 0
        else :
            word_list.append(letter)
    return 1

N = int(input())

sum = 0
for i in range(N) :
    sum += solution()

print(sum)