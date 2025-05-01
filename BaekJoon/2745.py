# 2025년 5월 1일
# 백준 2745번

line = input().split(' ')
N = line[0]
B = int(line[1])

letter_list = []
for letter in N :
    if ord(letter) >= 65 and ord(letter) < 91:
        letter_list.append(ord(letter)-55)
    elif ord(letter) >= 48 and ord(letter) < 58 :
        letter_list.append(ord(letter)-48)

sum = 0
total_digit = len(letter_list)
for i in range(total_digit) :
    digit = total_digit - i - 1
    sum += letter_list[i] * (B ** digit)

print(sum)
