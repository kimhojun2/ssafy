def f():
    result = 'YES'
    for l in lst:
        for r in lst:
            if r != l:
                if len(r) >= len(l):
                    if r[:len(l)] == l:
                        result = 'NO'
                        break

        if result == 'NO':
            break
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = []
    for n in range(N):
        lst.append(input())
    # result = 'YES'
    # for l in lst:
    #     for r in lst:
    #         if len(r) >= len(l):
    #             if r[:len(l)] == l:
    #                 result ='NO'
    #                 break
    #
    #     if result == 'NO':
    #         break
    print(f())