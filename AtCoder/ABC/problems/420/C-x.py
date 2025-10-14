# 変更はクエリごとに1回のみ　→　そこだけ変えればいい
N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0

for i in range(N):
    ans += min(A[i], B[i])

for i in range(Q):
    S = list(map(str, input().split()))

    x = int(S[1]) - 1
    y = int(S[2])

    ans -= min(A[x], B[x])

    if S[0] == "A":
        A[x] = y
    else:
        B[x] = y

    ans += min(A[x], B[x])

    print(ans)
