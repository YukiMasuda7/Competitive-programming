# list.remove(x)は先頭に近いxを"1個だけ"消す
# string.replace(a,b,n)はstring内のaをnこbに置き換える
Q = int(input())
box = []
for i in range(Q):
    S = list(map(str, input().split()))

    if S[0] == "1":
        box.append(int(S[1]))
    else:
        print(min(box))
        box.remove(min(box))
