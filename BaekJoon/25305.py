# 2025년 6월 1일 
# 백준 25305번

# 정렬에는 선택정렬, 삽입정렬, 버블정렬, 병합정렬, 힙 정렬 등이 있다.

# 선택정렬로 문제를 풀어보자
def selection_sort(num_list) :
    for num1 in range(len(num_list) - 1) :
        for num2 in range(num1 + 1, len(num_list)) :
            if num_list[num1] > num_list[num2] :
                temp = num_list[num1]
                num_list[num1] = num_list[num2]
                num_list[num2] = temp
    return num_list

# N, k 입력받기
N, k = map(int, input().split(' '))

# 성적을 리스트로 입력받기
score_list = list(map(int, input().split(' ')))

sorted_score_list = selection_sort(score_list)

print(sorted_score_list[-k])