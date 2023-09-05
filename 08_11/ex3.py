# N = int(input())
# evid = [0,-1, 1, 0, 2, 0, 3, 1, 4, 2, 5, 4, 4, 4]
# #1- 0 2-0 3-1 4-2 5-4 4-4
# timeStamp = [8,3,5,6,8,9,10]
# adj_m = [[0]*7 for _ in range(8)]
# visited = [0]*7
# for i in range(7):
#     v1, v2 = evid[i*2], evid[i*2+1]
#     adj_m[v1][v2] = 1
#     adj_m[v2][v1] = 1
# 
# print(adj_m)
# # def DFS(now):
# #     global visited
# #     now+1
# #     visited[now+1] = 1
# #     print(now+1)
# #     for j in range(7):
# #         print(i)
# #         if adj_m[now+1][i] == 1:
# #             DFS(i)
# #
# # DFS(5)

evid = [-1, 0, 0, 1, 2, 4, 4]
timeStamp = [8, 3, 5, 6, 8, 9, 10]
N = int(input())

def DFS(idx, time):
    if evid[idx] == -1:
        print(f'{idx}번 index(출발)')
        return 
    
    DFS(evid[idx], timeStamp[idx])
    print(f'{idx}번 index{timeStamp[idx]}시')

DFS(N, timeStamp[N])