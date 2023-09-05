T = int(input())
def ddd(arr):
    area_cnt = 0
    max_area = 0
    for i in range(N):
        for j in range(N):
            now = arr[i][j]
            for ni in range(i, N):
                for nj in range(j, N):
                    area = (ni - i + 1) * (nj - j + 1)
                    if arr[i][j] == arr[ni][nj]:
                        if area > max_area:
                            max_area = area
                            area_cnt = 0
                        if area == max_area:
                            area_cnt += 1

    return area_cnt

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]

    # area_cnt = 0
    # max_area = 0
    # for i in range(N):
    #     for j in range(N):
    #         now = arr[i][j]
    #         for ni in range(i, N):
    #             for nj in range(j, N):
    #                 area = (ni-i+1)*(nj-j+1)
    #                 if arr[i][j] == arr[ni][nj]:
    #                     if area > max_area:
    #                         max_area = area
    #                     if area == max_area:
    #                         area_cnt += 1
    r = ddd(arr)
    print(f'#{tc} {r}')


