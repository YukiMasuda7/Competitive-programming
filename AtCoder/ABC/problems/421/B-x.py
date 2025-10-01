# int(000123) は 123 (0は自動で省略される)
X, Y = map(int, input().split())
A = [0] * 10
A[0], A[1] = X, Y
for i in range(2, 10):
    a = A[i - 1] + A[i - 2]
    A[i] = int(str(a)[::-1])

print(A[9])
