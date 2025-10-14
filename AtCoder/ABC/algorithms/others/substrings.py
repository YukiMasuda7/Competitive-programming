# Sに含まれるすべての部分文字列を表現
S = input()
for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        substring = S[i:j]
        print(substring)
