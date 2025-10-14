# もっとも古いバージョンを管理する
N, Q = map(int, input().split())
pc = [1] * (N + 1)
pc[0] = 0
old = 1
for i in range(Q):
    X, Y = map(int, input().split())
    ans = 0
    while old <= X:
        ans += pc[old]
        pc[Y] += pc[old]
        old += 1
    print(ans)
