# def enQ(data):
#     global rear
#     if rear == len(Q)-1:
#         print('Q is Full')
#     else:
#         rear += 1
#         Q[rear] = data
#
#
#
# Q = [0] * 3
# rear = -1
# front = -1
#
# enQ(1)
# enQ(2)
# enQ(3)
# enQ(4)

'''
스택  : 후입선출 - 최근에 추가된 데이터가 먼저 삭제
append, pop
데이터 추가 :  push, 데이터 삭제 : pop
DFS로 활용

큐 :  선입선출 - 먼저 추가된 데이터가 먼저 삭제
데이터 추가 : enqueue, 데이터 삭제 : dequeue
append, pop(0)
'''
# from collections import deque
# # deque 양쪽 끝에서 삽입과 삭제가 이루어짐
# d = deque()
# d.append(1)
# d.extend([10, 15, 20])
# d.popleft()
# d.pop()
#
# for i in d:
#     print(i, end=' ')

def BFS(G, v):
    visited = [0]*(n+1)
    queue = []
    queue.append(v)
    while queue :
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = True
            visited(t)
            for i in G[t]:
                if not visited[i]:
                    queue.append(i)