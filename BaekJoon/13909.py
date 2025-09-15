# 2025년 6월 28일
# 백준 13909번

def main() :
    N = int(input())
    cnt = 0
    for i in range(1, N + 1) :
        if i * i <= N :
            cnt += 1
        elif i * i > N :
            break
    print(cnt)

if __name__ == "__main__" :
    main()