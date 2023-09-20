from collections import deque

def BFS(s, d):
    visited = [0]*1000001
    queue = deque()
    queue.append(s)
    visited[s] = 1
    while queue:
        t = queue.popleft()
        order = (t+1, t-1, t*2, t-10)
        for o in order:
            if 0< o<= 1000000:
                if not visited[o]:
                    visited[o] = visited[t] + 1
                    queue.append(o)
                    if o == d:
                        queue.clear()
                        break

    return visited[d]-1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = BFS(N,M)
    print(f'#{tc} {result}')