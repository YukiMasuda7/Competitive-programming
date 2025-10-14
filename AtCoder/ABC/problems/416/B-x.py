# 3**100は大きすぎるので全探索はだめ
# "#."を"#o"に置き換える　→　解に自由度の高いなら何か独自の規則を与える

S = input()
ans = list(S.replace("#.", "#o"))
if ans[0] == ".":
    ans[0] = "o"
ans = "".join(ans)
print(ans)
