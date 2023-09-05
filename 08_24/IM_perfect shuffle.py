T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(str, input().split()))
    if N%2 == 0:
        left = lst[0:N//2]
        right = lst[(N//2):]
    else:
        a = lst.pop(N//2)
        left = lst[0:N // 2]
        right = lst[(N // 2):]
        left.append(a)


    shuffle = []

    while left != [] or right != []:
        if left:
            shuffle.append(left.pop(0))
        if right:
            shuffle.append(right.pop(0))
    print(f'#{tc}', *shuffle)
