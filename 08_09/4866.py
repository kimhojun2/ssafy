T = int(input())
for tc in range(1, T + 1):
    code = list(input())
    stack = []
    result = 1
    for i in code:
        if i == '{' or i == '(':
            stack.append(i)

        elif i == ')':
            if len(stack) == 0 or stack[-1] !='(':
                result = 0
                break
            else:
                stack.pop()

        elif i == '}':
            if len(stack) == 0 or stack[-1] !='{':
                result = 0
                break
            else:
                stack.pop()

    if len(stack) != 0:
        result = 0

    print(f'#{tc} {result}')
