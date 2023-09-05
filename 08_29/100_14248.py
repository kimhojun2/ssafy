from collections import deque
n = int(input())
arr = list(map(int, input().split()))
s = int(input())
visited = [0]*(n+1)
visited[s] = 1
queue = deque()
queue.append(s)

while queue:
    r = queue.popleft()
    left_r, right_r = r - arr[r-1], r + arr[r-1]
    if 1<= left_r:
        visited[left_r] = 1
        queue.append(left_r)
    if right_r <= n:
        visited[right_r] = 1
        queue.append(right_r)

print(visited.count(1))
