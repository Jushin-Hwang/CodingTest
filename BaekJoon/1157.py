# 2025년 4월 28일
# 백준 1157번

word = input()
word = word.upper()

word_dict = {}

for spelling in list(word) :
    if spelling in word_dict :
        word_dict[spelling] += 1
    else :
        word_dict[spelling] = 1

word_dict_values = word_dict.values()

max_value = max(word_dict_values)
count = 0
for value in word_dict_values :
    if value == max_value :
        count += 1

if count > 1 :
    print("?")
else :
    key = [k for k, v in word_dict.items() if v == max_value]
    print(key[0])