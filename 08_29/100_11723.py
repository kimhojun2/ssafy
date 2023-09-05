from collections import deque
S = deque()
M = int(input())
for m in range(M):
    a = list(input().split())
    if len(a) == 2:
        w, num = a[0], a[1]
    else:
        w = a[0]

    if w == 'add':
        if num not in S:
            S.append(num)
    elif w == 'remove':
        if num in S:
            S.remove(num)
    elif w == 'check':
        if num in S:
            print(1)
        else:
            print(0)
    elif w == 'toggle':
        if num in S:
            S.remove(num)
        else:
            S.append(num)
    elif w == 'all':
        S = deque([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    elif w == 'empty':
        S = deque()
