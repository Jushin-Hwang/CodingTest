# 2024년 9월 5일 
# 백준 5622번

char_to_int = [[], [], [] , ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]

def solution(sum, c) :
    for i in range(len(char_to_int)) :
        for j in range(len(char_to_int[i])) :
            if char_to_int[i][j] == c :
                sum += i
                return sum

# Main Function
sum = 0

word = input()

for i in range(len(word)) :
    c = word[i]
    sum = solution(sum, c)

print(sum)