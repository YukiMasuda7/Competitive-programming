# 持つ/持たない などの2択の全パターンを列挙する
# 例 : 2部グラフ
# 1つ目のforで全列挙
# 2つ目のforで各桁に注目
N = int(input())
for bit in range(2**N):
    for shift in range(N):
        if bit << shift & 1:
            print("Yes")
