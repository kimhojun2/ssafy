T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split()))for _ in range(9)]
    box = [0, 3, 6]
    result = 1
    if result == 1:
        for i in range(9):
            ans_x = set()
            for j in range(9):
                ans_x.add(arr[i][j])

            if set(range(1, 10)) != ans_x:
                result = 0
                break

            if result == 0:
                break
    if result == 1:
        for x in range(9):
            ans_y = set()
            for y in range(9):
                ans_y.add(arr[y][x])

            if set(range(1,10)) != ans_y:
                result = 0
                break

            if result == 0:
                break

    if result == 1:
        for z in box:
            for zz in box:
                arr_box = set()
                for m in range(3):
                    for mm in range(3):
                        arr_box.add(arr[z+m][zz+mm])

                if set(range(1,10)) != arr_box:
                    result = 0
                    break
            if result == 0:
                break



    print(f'#{tc} {result}')