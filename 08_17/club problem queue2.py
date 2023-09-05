from collections import deque

clock = deque([12, 3, 6, 9])
turn = int(input()) // 90
clock.rotate(turn)
print(clock[0],clock[3], clock[1], clock[2])

K = int(input()) // 90
clock = [3, 6, 9, 12]
order = [3, 2, 0, 1]

for i in range(K):
    clock.insert(0, clock.pop())

for i in order:
    print(clock[i], end=' ')

arr = [12, 9, 3, 6]
