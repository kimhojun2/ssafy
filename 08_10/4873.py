T = int(input())
for tc in range(1, T+1):
    S = list(input())
    stack = []
    for s in S:
        if len(stack) == 0:
            stack.append(s)

        else:
            if stack[-1] == s:
                stack.pop()

            else:
                stack.append(s)

    print(f'#{tc} {len(stack)}')
