#딱지놀이
# 별 동그라미 네모 세모 무승부
N = int(input())
for n in range(N):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ai = a.pop(0)
    bi = b.pop(0)

    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)
    # print(a, b)
    i = 0
    result = True
    while i < len(a) and i < len(b):
        if a[i] > b[i]:
            result = False
            print('A')
            break
        elif a[i] < b[i]:
            result = False
            print('B')
            break
        i += 1

    if result == True:
        if len(a) > len(b):
            print('A')
        elif len(a) < len(b):
            print('B')
        else:
            print('D')
