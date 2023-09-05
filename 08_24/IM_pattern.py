def f(p):
    i = 1
    max_m = 10e5
    while i <= 11:
        m = p[0:i]
        t = p[0:30 - (30 % len(m))]
        if t.count(m) * len(m) == len(t):
            print(f'#{tc} {len(m)}')
            break
            # if max_m > i:
            #     max_m = i
        i += 1

T = int(input())
for tc in range(1, T+1):
    p = input()
    # i = 1
    # max_m = 10e5
    # while i <= 11:
    #     m = p[0:i]
    #     p = p[0:30-30%len(m)]
    #     if p.count(m)*len(m) == len(p):
    #         print(len(m))
    #         break
    #         # if max_m > i:
    #         #     max_m = i
    #     i += 1
    # print(f'#{tc} {max_m}')
    f(p)
