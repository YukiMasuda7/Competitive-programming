N, L, R = map(int, input().split())
S = input()
sub_S = S[L - 1 : R]
for c in sub_S:
    if c == "x":
        print("No")
        exit()
print("Yes")
