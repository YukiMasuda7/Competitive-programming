from collections import defaultdict

S = input()
D = defaultdict(int)
for s in S:
    D[s] += 1
