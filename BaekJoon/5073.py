# 2025년 5월 14일
# 백준 5073번

def solution(num_list) :
    new_num_list = [int(num) for num in num_list]
    max_num = max(new_num_list)
    new_num_list.remove(max_num)

    if sum(new_num_list) <= max_num :
        return "Invalid"
    
    new_num_list.append(max_num)
    if len(set(new_num_list)) == 1 :
        return "Equilateral"
    elif len(set(new_num_list)) == 2 :
        return("Isosceles")
    else :
        return "Scalene"

    
while(True) :
    num_list = input().split(' ')
    if set(num_list) == {'0'} :
        break
    else :
        print(solution(num_list))