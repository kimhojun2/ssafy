# N = int(input())
# arr = [list(map(int, input().split()))for _ in range(N)]
# print(arr)

# N = 2
# M = 4
#
# arr = [[0, 1, 2, 3], [4, 5, 6, 7]]


# 행 우선 순회
# for i in range(N):
#     for j in range(M):
#         print(arr[i][j])

# 열 우선 순회
# for i in range(M):
#     for j in range(N):
#         print(arr[j][i])

#지그재그 순회

# for i in range(N):
#     for j in range(M):
#         if i%2==1:  # 홀수번 행인 경우
#             print(arr[i][M-1-j])
#         else:   # 짝수번 행인 경우
#             print(arr[i][j])
#         # print(arr[i][j + (M-1-2*j)*(i%2)])


# 빈 2차원 행렬 만들기
# arr = [[0]*M for _ in range(N)]
# print(arr)

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]

max_v = 0
for i in range(N):
    for j in range(N):
        # arr[i][j]중심으로
        s = arr[i][j]
        for k in range(4): # for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]
            # for p in range(m)
            ni, nj = i+di[k], j+dj[k]
            if 0 <=ni<N and 0<=nj<N:
                s += arr[ni][nj]
        # 여기까지 주변 원소를 포함한 합
        if max_v < s:
            max_v = s
print(max_v)

# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# total1 = 0
# totla2 = 0
# for i in range(N):
#     total1 += arr[i][i]
#
# for i in range(N):
#     totla2 +=arr[i][N-1-i]
#
# print(total1)
# print(totla2)