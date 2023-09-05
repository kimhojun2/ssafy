from collections import deque

def BFS(s, d):
    visited = [0]*100001
    queue = deque()
    queue.append(s)
    lst = [[0,0,0,0,0]for _ in range(1000001)]

    while queue:
        t = queue.popleft()
        order = [t+60,t+10,t-10,t+1,t-1]
        for o in order:
            if 0 <= o <= 100000:
                if not visited[o]:
                    visited[o] = visited[t] + 1
                    lst[o] = lst[t].copy()
                    lst[o][order.index(o)] += 1
                    queue.append(o)
                    if o == d:
                        queue.clear()
                        break


    print(lst[d])


T = int(input())
for tc in range(1, T+1):
    D = int(input())
    BFS(0,D)