
def ddd(PS):
    stack = []
    for i in PS:
        if len(stack) == 0:
            stack.append(int(i))

        else:
            if int(i) == stack[-1]:
                stack.pop()
            else:
                stack.append(int(i))
    return stack

for tc in range(1, 11):
    N, ps = map(str, input().split())
    PS = list(ps)
    result1 = ddd(PS)
    result = ''.join(map(str, ddd(PS)))

    print(f'#{tc} {result}')
