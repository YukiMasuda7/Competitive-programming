N = int(input())
S = []
for _ in range(N):
    s = str(input())
    S.append(s)
T = list(map(str, input().split()))
x = int(T[0]) - 1
y = T[1]

if S[x] == y:
    print("Yes")
else:
    print("No")
