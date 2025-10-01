# 順列全探索
# memo
# まずは全探索のような愚直な方法を試す
from itertools import permutations

N = int(input())
A = list(map(int, input().split()))

for permutation in permutations(i + 1 for i in range(N)):
    flag = True
    for i in range(N):
        if A[i] != -1 and A[i] != permutation[i]:
            flag = False
    if flag:
        print("Yes")
        print(*permutation)
        exit()
print("No")
