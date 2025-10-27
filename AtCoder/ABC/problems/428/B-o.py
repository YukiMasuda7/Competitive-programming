from collections import defaultdict

d = defaultdict(int)
N, K = map(int, input().split())
S = input()
for i in range(0, len(S) - K + 1):
    substring = S[i : i + K]
    d[substring] += 1
sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
max_count = sorted_d[0][1]
ans = []
for i in range(len(sorted_d)):
    if sorted_d[i][1] == max_count:
        ans.append(sorted_d[i][0])
ans.sort()

print(max_count)
print(*ans)
