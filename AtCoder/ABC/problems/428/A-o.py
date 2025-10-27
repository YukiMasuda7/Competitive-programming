S, A, B, X = map(int, input().split())

n = X // (A + B)
r = X % (A + B)

if 0 <= r <= A:
    ans = S * (n * A + r)
else:
    ans = S * (n + 1) * A
print(ans)
