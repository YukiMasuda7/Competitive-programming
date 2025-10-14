# 部分文字列の全列挙
S = input()
ans = 0
for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        substring = S[i:j]
        if substring[0] == "t" and substring[-1] == "t" and len(substring) >= 3:
            t_count = 0
            for c in substring:
                if c == "t":
                    t_count += 1
            sub_ans = (t_count - 2) / (len(substring) - 2)
            ans = max(sub_ans, ans)

print(ans)
