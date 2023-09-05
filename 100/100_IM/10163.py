N = int(input())
arr = [[0]*1001for _ in range(1001)]
paper = [0]*(N+1)
for n in range(1, N+1):
    x, y, W, H = map(int, input().split())
    for w in range(W):
        for h in range(H):
            if arr[y+h][x+w] == 0:
                arr[y+h][x+w] = n
                paper[n] +=1
            else:
                paper[arr[y+h][x+w]] -=1
                arr[y+h][x+w] = n
                paper[n] +=1




paper.pop(0)
for p in paper:
    print(p)
