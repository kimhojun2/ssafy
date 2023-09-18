from collections import deque
S = list(input())
stack = deque()
total = 0
check = 0
last = 'a'
for s in S:
    if s.isdigit() == True:
        stack.append(int(s))
    elif s =='+':
        if not check:
            z = 0
            while stack:
                n = stack.pop()
                total += n*10**z
                z += 1
        else:
            z = 0
            while stack:
                n = stack.pop()
                total -= n * 10 ** z
                z += 1
    elif s =='-':
        if not check:
            check = 1
            z = 0
            while stack:
                n = stack.pop()
                total += n * 10 ** z
                z += 1
        else:
            z = 0
            while stack:
                n = stack.pop()
                total -= n * 10 ** z
                z += 1
if stack:
    if check:
        z = 0
        while stack:
            n = stack.pop()
            total -= n * 10 ** z
            z += 1
    else:
        z = 0
        while stack:
            n = stack.pop()
            total += n * 10 ** z
            z += 1

print(total)