def win(x, y):
    if arr[x] == arr[y]:
        return x
    elif arr[x] - arr[y] == 1 or arr[x] - arr[y] == -2:
        return x

    return y

def group(start, end):
    if start == end:
        return start

    left = group(start, (start+end)//2)
    right = group((start+end)//2 + 1, end)

    return win(left, right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = group(0, N-1) + 1
    print(f'#{tc} {result}')