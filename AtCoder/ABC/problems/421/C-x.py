# 操作は入れ替えだけ　→　AとBの数はそれぞれ変わらない
# 答えは ABABAB... or BABABA... のみ
# Sの前からk番目のAとTの前からk番目のAは同じ位置
# 一つ移動させるためのコストは1

N = int(input())
S = input()

T1 = ["AB"] * N
T2 = ["BA"] * N

AinS = []
for i in range(2 * N):
    if S[i] == "A":
        AinS.append(i)

ans1 = 0
ans2 = 0

for i in range(N):
    ans1 += abs(AinS[i] - 2 * i)
    ans2 += abs(AinS[i] - (2 * i + 1))
ans = min(ans1, ans2)
print(ans)
