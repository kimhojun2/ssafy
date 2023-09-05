# 의석이
def f(arr):
    len_arr = []
    for l in arr:
        len_arr.append(len(l))
    word = ''
    n = 0
    while n <= max(len_arr):
        if [] not in arr:
            for i in range(len(arr)):
                word += arr[i][0]
                arr[i].pop(0)
            n += 1

        else:
            while [] in arr:
                a = arr.index([])
                arr.pop(a)


    return word

T = int(input())
for tc in range(1, T+1):
    arr = [list(input())for _ in range(5)]
    # len_arr = []
    # for l in arr:
    #     len_arr.append(len(l))
    # word = ''
    # j = 0
    # while j < max(len_arr):
    #     if [] not in arr:
    #         for i in range(5):
    #             word += arr[i][j]
    #     else:
    #         break
    # print(word)
    print(f'#{tc} {f(arr)}')