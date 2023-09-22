# 인수의 생일 파티
from collections import deque

def DFS(start):
    stack = deque()
    stack.append(start)
    while stack:
        now = stack.pop()





T = int(input())
for tc in range(1, T+1):
    N,M,X = map(int, input().split())
    graph = [[0] * (N+1) for _ in range(N+1)]
    visited = [0]*N+1
    for _ in range(M):
        s, e, t = map(int, input().split())
        graph[s][e] = t
