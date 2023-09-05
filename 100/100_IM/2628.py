#종이 자르기
from collections import deque
W, H = map(int, input().split())
arr = [[0]*(W+1)for _ in range(H+1)]
N = int(input())
ga = [0, W]
se = [0, H]
for n in range(N):
    d, s = map(int, input().split())
    if d == 0:
        se.append(s)
    else:
        ga.append(s)

ga.sort()
se.sort()
max_square = 0
for i in range(len(ga)-1):
    for j in range(len(se)-1):
        square = (ga[i+1]-ga[i])*(se[j+1]-se[j])
        if square > max_square:
            max_square = square

print(max_square)
