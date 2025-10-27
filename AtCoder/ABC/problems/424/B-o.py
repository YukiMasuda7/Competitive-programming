N, M, K = map(int, input().split())
AC = [[] for _ in range(N)]
ans = []
for i in range(K):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    AC[A].append(B)
    if len(AC[A]) == M:
        ans.append(A + 1)
print(*ans)
