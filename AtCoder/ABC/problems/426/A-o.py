X, Y = map(str, input().split())

if X == Y:
    ans = "Yes"
elif X == "Lynx" and (Y == "Serval" or Y == "Ocelot"):
    ans = "Yes"
elif X == "Serval" and Y == "Ocelot":
    ans = "Yes"
else:
    ans = "No"
print(ans)
