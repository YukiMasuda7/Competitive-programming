# s=list(s)で一文字ずつ区切れる


def split_num(n: str):
    S = list(n)
    T = []
    for c in S:
        T.append(int(c))
    return sum(T)


N = int(input())

if N == 0:
    ans = 1
else:
    ans = 1
    for i in range(2, N + 1):
        ans += split_num(str(ans))
print(ans)
