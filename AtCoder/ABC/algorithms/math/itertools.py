from itertools import combinations, permutations, product

# 順列
items = ["A", "B", "C"]
for permutation in permutations(items, 2):
    print(permutation)
# 出力: ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')
# for p in permutations([i + 1 for i in range(n)]): で1からNの数字の順列

# 組み合わせ
items = ["A", "B", "C"]
for combination in combinations(items, 2):
    print(combination)
# 出力: ('A', 'B'), ('A', 'C'), ('B', 'C')

# 直積
for product in product([1, 2], ["A", "B"]):
    print(product)
# 出力: (1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')
