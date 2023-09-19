def backtracking(sum, n, current):
    global cnt
    if sum == n:
        cnt += 1
        return

    if sum > n:
        return

    for num in range(1, 4):
        current.append(num)
        backtracking(sum + num, n, current)
        current.pop()

cnt = 0
n = int(input())
backtracking(0, n, [])
print(cnt)

