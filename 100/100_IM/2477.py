from collections import deque
arr = [[0]*21for _ in range(21)]
K = int(input())
y = 10
x = 10
for i in range(6):
    d, l = map(int, input().split())
    if d == 1:
        for a in range(l):
            arr[y][x+a] = 1
        x += l

    elif d == 2:
        for b in range(l):
            arr[y][x-b] = 1
        x -= l

    elif d == 3:
        for c in range(l):
            arr[y+c][x] = 1
        y += l

    elif d == 4:
        for e in range(l):
            arr[y-e][x] = 1
        y -= l
cnt = 0
for z in range(21):
    for zz in range(21):
        if arr[z][zz] == 1:
            cnt += 1
print(cnt)
print(arr)