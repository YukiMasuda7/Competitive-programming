N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for b in B:
    for a in A:
        if b == a:
            A.remove(a)
            break
print(*A)
