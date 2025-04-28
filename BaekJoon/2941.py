# 2025년 4월 28일
# 백준 2941번

word = input()

word = word.replace("c=", "č")
word = word.replace("c-", 'ć')
word = word.replace('d-', 'ž')
word = word.replace('dz=', 'đ')
word = word.replace('lj', 'ž')
word = word.replace('nj', 'ž')
word = word.replace('s=', 'š')
word = word.replace('z=','ž')

print(len(word))