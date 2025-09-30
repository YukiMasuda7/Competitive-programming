from collections import deque

d = deque([1, 2, 3])

# 末尾に追加・削除 O(1)
d.append(4)
d.pop()

# 先頭に追加削除 O(1)
d.appendleft(0)
d.popleft()
