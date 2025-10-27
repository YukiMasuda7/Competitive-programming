a, b, c = map(int, input().split())
if a == b or b == c or c == a:
    ans = "Yes"
else:
    ans = "No"
print(ans)
