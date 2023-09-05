N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

min_total = 0
numbers = {}
for i in range(N):
    b = B.pop(B.index(max(B)))
    a = A.pop(A.index(min(A)))
    min_total += a * b
print(min_total)