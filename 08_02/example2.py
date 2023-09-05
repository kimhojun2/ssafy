arr = []
for i in range(4):
    a = []
    for j in range(5):
        a.append('_')
    arr.append(a)
Y_1, X_1 = map(int, input().split())
Y_2, X_2 = map(int, input().split())

for i in range(4):
    for j in range(5):
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0], [1,1], [1,-1], [-1,1], [-1,-1]]:
            ni, nj = i+di, j+dj
            if 0 <=ni<5 and 0<=nj<4:
                arr[ni][nj] = "#"
        # 여기까지 주변 원소를 포함한 합
print(arr)

