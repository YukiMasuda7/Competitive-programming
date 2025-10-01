N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]
score = [0] * N
ans = []

for i in range(M):
    count_0 = 0
    for j in range(N):
        if S[j][i] == "0":
            count_0 += 1

    if count_0 < N // 2 + 1:
        minority = "0"
    else:
        minority = "1"

    for j in range(N):
        if S[j][i] == minority:
            score[j] += 1

max_score = max(score)
for i in range(N):
    if score[i] == max_score:
        ans.append(i + 1)

print(*ans)
