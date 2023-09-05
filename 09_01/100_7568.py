N = int(input())
arr = []
rank = []
for n in range(N):
    w, k = map(int, input().split())
    arr.append((w, k))

for i in range(N):
    cnt = 0
    for j in range(N):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt += 1
    rank.append(cnt + 1)

print(*rank)