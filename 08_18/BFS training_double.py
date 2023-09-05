from collections import deque

def BFS(s, d):
    visited = [0]*100001
    queue = deque()
    queue.append(s)
    visited[s] = 1
    while queue:
        t = queue.popleft()
        order = [t//2,t*2,t+1,t-1]
        for o in order:
            if 0<= o<= 100000:
                if not visited[o]:
                    visited[o] = visited[t] + 1
                    queue.append(o)
                    if o == d:
                        queue.clear()
                        break

    print(visited[d]-1)


S = int(input())
D = int(input())
BFS(S, D)