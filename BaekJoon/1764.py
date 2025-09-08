# 2025년 6월 17일
# 백준 1764번

# Import modules
import sys

# Get N, M inputs
N, M = map(int, input().split())

# Declare a set variables
unheard_set = set() # N
unseen_set = set() # M

# Make Set list
for _ in range(N) :
    unheard_set.add(sys.stdin.readline().strip())

for __ in range(M) :
    unseen_set.add(sys.stdin.readline().strip())

# Get intersection between unheard_set and unseen_set
result = list(unheard_set.intersection(unseen_set))
result.sort()

print(len(result))
for name in result :
    print(name)