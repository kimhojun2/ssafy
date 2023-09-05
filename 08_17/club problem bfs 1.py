def BFS(G, v):
    visited = [0]*6
    queue = []
    queue.append(v)
    visited[v] = 1
    print(v)
    while queue:
        t = queue.pop(0)
        for i in range(6):
            if not visited[i] and arr[t][i] == 1:
                visited[i] = 1
                queue.append(i)
                print(i)





arr = [[0,0,0,0,1,0],
       [1,0,1,0,0,1],
       [1,0,0,1,0,0],
       [1,1,0,0,0,0],
       [0,1,0,1,0,1],
       [0,0,1,1,0,0]]
n = int(input())
BFS(arr, n)