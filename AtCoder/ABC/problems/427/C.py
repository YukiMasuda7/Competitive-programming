# 頂点の塗り方を全部試す(bit全探索でO(2**N))
# すべての辺について同じ色であれば(これが消すべき辺)delete_count+=1
# delete_countの最小値が答え

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

ans = 10**10
for bit in range(2**N):
    delete_count = 0
    for edge in edges:
        if (1 & (bit >> edge[0] - 1)) == (1 & (bit >> edge[1] - 1)):
            delete_count += 1
    ans = min(ans, delete_count)
print(ans)
