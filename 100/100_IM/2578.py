#빙고
def f(arr):
    ans = 0
    for y in range(5):
        if sum(arr[y]) == 0:
            ans += 1

    for xx in range(5):
        sero = 0
        for yy in range(5):
            if arr[yy][xx] == 0:
                sero += 1
        if sero == 5:
            ans += 1

    right_dae = 0
    left_dae = 0
    for l in range(5):
        if arr[l][l] == 0:
            right_dae +=1
        if arr[l][4-l] == 0:
            left_dae +=1
    if right_dae == 5:
        ans += 1
    if left_dae == 5:
        ans += 1

    if ans >= 3:
        return 3
    else:
        return 0




arr = [list(map(int, input().split()))for _ in range(5)]
lst = []
for i in range(5):
    a = list(map(int, input().split()))
    lst.append(a)
cnt = 0
for ly in range(5):
    for lx in range(5):
        for ay in range(5):
            for ax in range(5):
                if lst[ly][lx] == arr[ay][ax]:
                    arr[ay][ax] = 0
                    cnt += 1
                    result = f(arr)
                    if result >= 3:
                        print(cnt)
                        exit()