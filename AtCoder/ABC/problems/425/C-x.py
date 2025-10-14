# %で回転処理、lとrの反転を防ぎたい　→　長さ2Nの配列を用意する
# 1-indexで扱えるように工夫

N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = [0] + A + A
S = [0] * (2 * N + 1)
rotate = 0

for i in range(1, 2 * N + 1):
    S[i] = S[i - 1] + B[i]

for i in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        rotate = (rotate + query[1]) % N
    else:
        l = query[1] + rotate
        r = query[2] + rotate
        ans = S[r] - S[l - 1]
        print(ans)
