def f(origial):
    reset = ['0'] * len(original)
    cnt = 0
    l = 0
    while l < len(original):
        if reset[l] != original[l]:
            for r in range(l, len(reset)):
                reset[r] = original[l]
            cnt += 1

        l += 1

    return cnt

T = int(input())
for tc in range(1, T+1):
    original = list(str(input()))
    # print(original)
    # reset = [0]*len(original)
    # cnt = 0
    # l = 0
    # while l < len(original):
    #     if reset[l] != original[l]:
    #         for r in range(l, len(reset)):
    #             reset[r] = original[l]
    #         cnt += 1
    #
    #     l += 1
    print(f'#{tc} {f(original)}')
