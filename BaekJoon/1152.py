# 2024년 9월 4일 
# 백준 1152번
# 수정 1) 공백으로 시작하거나, 공백으로 끝날 경우를 고려한다.


def solution() :
    count = 0

    sentence = input()

    if sentence[0] == ' ':
        count -= 1

    if sentence[len(sentence) - 1] == ' ' :
        count -= 1
        
    for i in range(len(sentence)) :
        if sentence[i] == ' ' :
            count += 1

    return count + 1

# Main Function
print(solution())