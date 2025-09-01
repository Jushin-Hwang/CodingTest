# 2025년 5월 29일 
# 백준 2750번

# 함수 정의
def bubble_sort(data) : # 버블정렬
    for i in range(howmany - 1) :
        for j in range(howmany - i - 1) :
            if data[j] > data[j+1] :
                data[j], data[j+1] = data[j+1], data[j]
            
def print_data(data) : # 데이터 출력
    for i in range(len(data)) :
        print(data[i])

howmany = int(input())
data = []

for _ in range(howmany) :
    data.append(int(input()))

bubble_sort(data)
print_data(data)