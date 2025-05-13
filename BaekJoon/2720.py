# 2025년 5월 1일
# 백준 2720번

T = int(input())

def remain_cents(cents, divisor) :
    howmany = cents // divisor
    remain = cents % divisor
    return howmany, remain

def solution() :
    cents = int(input())
    quarter, cents = remain_cents(cents, 25)
    dime, cents = remain_cents(cents, 10)
    nickel, penny = remain_cents(cents, 5)
    print(f"{quarter} {dime} {nickel} {penny}")

def main(Test_case) :
    for _ in range(Test_case) :
        solution()

main(T)