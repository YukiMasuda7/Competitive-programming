from collections import defaultdict

S = input()
D = defaultdict(int)

for s in S:
    D[s] += 1

for d in D:
    if D[d] == 1:
        print(d)
