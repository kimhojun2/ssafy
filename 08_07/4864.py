T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input())for _ in range(N)]
    # print(arr)
    result = []
    for i in range(N):
        for j in range(N):
            word_x = []
            for x in range(M):
                nj = j + x
                if 0 <= nj < N:
                    word_x.append(arr[i][nj])
                if len(word_x) == M and word_x == list(reversed(word_x)):
                    result = word_x
            word_y = []
            for y in range(M):
                ni = i + y
                if 0 <= ni < N:
                    word_y.append(arr[ni][j])
                if len(word_y) == M and word_y == list(reversed(word_y)):
                    result =word_y

    print(f'#{tc} {"".join(result)}')