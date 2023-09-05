from collections import deque
N = int(input())
arr = list(map(int, input().split()))

def f(N):
    line = []
    for i in range(0, N):
        line.insert(arr[i], i+1)
    return list(reversed(line))
result = f(N)
print(*result)

