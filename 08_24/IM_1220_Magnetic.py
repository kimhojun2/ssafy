def f(N, arr):
    cnt = 0
    for j in range(N):
        lst = []
        for i in range(N):
            lst.append(arr[i][j])
        lst = list(filter(lambda value: value != 0, lst))

        while lst:
            if lst[0] == 2:
                lst.pop(0)
            else:
                break

        while lst:
            if lst[-1] == 1:
                lst.pop()
            else:
                break
        #
        # print(lst)
        # print(cnt)

        if lst:
            stack = []
            for z in range(len(lst)):
                if len(stack) == 0:
                    stack.append(lst[z])
                else:
                    if stack[-1] == 2:
                        stack.append(lst[z])

                    elif stack[-1] == 1:
                        if lst[z] == 1:
                            stack.append(lst[z])
                        else:
                            stack.clear()
                            stack.append(lst[z])
                            cnt += 1



    return cnt


for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    # 1 : N극       2 :  S극
    # cnt = 0
    # for j in range(N):
    #     lst = []
    #     for i in range(N):
    #         lst.append(arr[i][j])
    #     lst = list(filter(lambda value: value != 0, lst))
    #
    #
    #     while lst:
    #         if lst[0] == 1:
    #             lst.pop(0)
    #         else:
    #             break
    #
    #
    #     while lst:
    #         if lst[-1] == 2:
    #             lst.pop()
    #         else:
    #             break
    #
    #     print(lst)
    #
    #     stack = []
    #     for z in lst:
    #         if len(stack) == 0:
    #             stack.append(z)
    #         else:
    #             if stack[-1] == 2:
    #                 stack.append(z)
    #
    #             elif stack[-1] == 1:
    #                 if z == 1:
    #                     stack.append(z)
    #                 else:
    #                     stack.clear()
    #                     stack.append(z)
    #                     cnt+=1
    result = f(N,arr)
    print(f'#{tc} {result}')
    # print(f'#{tc} {cnt}')

