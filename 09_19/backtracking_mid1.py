

def backtracking1(cnt,N):
    if cnt == N:
        print(*path)
        return

    for num in range(1,7):
        path[cnt] = num
        backtracking1(cnt+1, N)
        path[cnt] = 0


def backtracking3(cnt, N, start):
    if cnt == N:
        print(*path)
        return

    for i in range(start, 7):
        path[cnt] = i
        backtracking3(cnt + 1, N, i + 1)


def backtracking2(cnt, N, start):
    if cnt == N:
        print(*path)
        return

    for i in range(start, 7):
        path[cnt] = i
        backtracking2(cnt + 1, N, i)


N, M = map(int, input().split())
path = [0]*N
if M == 1:
    backtracking1(0, N)
elif M == 2:
    backtracking2(0,N,1)
elif M ==3:
    backtracking3(0,N,1)
