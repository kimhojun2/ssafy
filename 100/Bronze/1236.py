N, M = map(int, input().split())

arr = [list(map(str, input()))for _ in range(N)]

count_y = 0
count_x = 0


for i in range(N):
    lst_x = []
    for j in range(M):
        lst_x.append(arr[i][j])
    if "X" not in lst_x:
        count_x += 1

for l in range(M):
    lst_y = []
    for k in range(N):
        lst_y.append(arr[k][l])
    if "X" not in lst_y:
        count_y += 1

print(max(count_x, count_y))
