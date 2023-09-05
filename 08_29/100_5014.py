from collections import deque
def BFS(F,S,G,U,D):
    queue = deque()
    visted = [0]*(F+1)
    queue.append(S)
    visted[S] = 1
    up = 0
    down = 0
    while queue:
        # if visted[G] == 1:
        #     print()

        now = queue.popleft()
        next_up = now + 1
        next_down = now - 1
        if not visted[next_up] and 1 <= next_up <= (F):
            visted[next_up] = 1
            queue.append(next_up)
            up += 1
        if not visted[next_down] and 1 <= next_down <=(F):
            visted[next_down] = 1
            queue.append(next_down)
            down += 1

    if up > U or down > D:
        return print('use the stairs')




F,S,G,U,D = map(int, input().split())
BFS(F,S,G,U,D)