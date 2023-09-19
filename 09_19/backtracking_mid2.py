def backtracking(cnt):
    global result
    if cnt == 3:
        result += 1
        return

    for num in arr:
        if num in path:
            continue

        path[cnt] = num
        backtracking(cnt+1)
        path[cnt] = 0

N = int(input())
arr = [i for i in range(1,N+1)]
path = [0]*3
result = 0
backtracking(0)
print(result)

