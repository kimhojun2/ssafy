T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [[0]*10 for _ in range(10)]
    result = 0
    for k in range(N):
        red1, blue1, red2, blue2, color = map(int, input().split())

        for i in range(red1, red2 + 1):
            for j in range(blue1, blue2 + 1):
                arr[i][j] += color
                # 격자 값이 3이면 카운팅

                if arr[i][j] == 3:
                    result += 1

    print(f"#{tc} {result}")