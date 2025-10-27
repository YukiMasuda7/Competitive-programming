# "(" を +1, ")" を -1 として数の遷移をAで管理、それまで最小値をBで管理する
# Aが0になる → "(" と ")" の数が釣り合う
# Bが負 → 途中に閉じすぎ。 ")"が多すぎてそれ以降絶対に良い括弧列ができない状態 )
# 直前の操作をO(1)で消したい　→　スタック
from collections import deque

inf = 10**10
Q = int(input())
A = deque([0])
B = deque([inf])
for i in range(Q):
    q = list(map(str, input().split()))
    if q[0] == "1":
        add = 1 if q[1] == "(" else -1
        A.append(A[-1] + add)
        B.append(min(B[-1], A[-1]))
    else:
        A.pop()
        B.pop()
    if A[-1] == 0 and (B[-1] == 0 or B[-1] == inf):
        ans = "Yes"
    else:
        ans = "No"
    print(ans)
