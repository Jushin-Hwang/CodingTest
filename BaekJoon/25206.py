# 2025년 5월 1일
# 백준 25206번

sum_score = 0
sum_point = 0
for i in range(20) :
    input_list = list(input().split(' '))
    subject = input_list[0]
    score = float(input_list[1])
    grade = input_list[2]

    if grade == 'P' :
        continue
    elif grade == 'A+' :
        grade_point = 4.5
    elif grade == 'A0' :
        grade_point = 4.0
    elif grade == 'B+' :
        grade_point = 3.5
    elif grade == 'B0' :
        grade_point = 3.0
    elif grade == 'C+' :
        grade_point = 2.5
    elif grade == 'C0' :
        grade_point = 2.0
    elif grade == 'D+' :
        grade_point = 1.5
    elif grade == 'D0' :
        grade_point = 1.0
    elif grade == 'F' :
        grade_point = 0.0
    sum_point += (grade_point * score)
    sum_score += score

average = sum_point / sum_score

print(average)
