T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    C = list(map(int, input().split()))
    T = list(map(int, input().split()))
    C.sort(reverse=True)
    T.sort(reverse=True)
    weight = 0
    cnum = 0
    while cnum < len(C):
        c = C[cnum]
        for t in T:
            if c <= t:
                weight += c
                T.pop(T.index(t))
                break
        cnum += 1
    print(f'#{tc} {weight}')