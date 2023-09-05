def check(form):
    stack = []
    for tk in form:
        if tk in ['(', '{']:
            stack.append(tk)
        elif tk == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return 0

        elif tk =='}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                return 0

    return 0 if stack else 1


def op(form):
    stack = []
    for tk in form:
        if tk == ')':
            tmp = 0
            while stack and stack[-1] != '(':
                tmp += int(stack.pop()) # 덧셈연산
            stack.pop()
            stack.append(tmp)

        elif tk == '}':
            tmp = 1
            while stack and stack[-1] != '{':
                tmp *= int(stack.pop())  # 곱셈연산
            stack.pop()
            stack.append(tmp)
        else:
            stack.append(tk)

    return -1 if len(stack) != 1 else stack[0]


T = int(input())
for tc in range(1, T+1):
    form = input()
    ans = -1
    if check(form):
        ans = op(form)
    print(f'#{tc} {ans}')