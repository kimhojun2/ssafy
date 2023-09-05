T = int(input())
for tc in range(1,T+1):
    code = list(input())
    stack = []
    top = -1    # 후입선출 되는 index
    result = 0
    for i in code:
        if result == -1:    # result 값이 -1이면 종료한다
            break

        elif len(stack) != 0:

            if i == '(' or i == '{':    # 괄호의 여는 부분이 들어오면 stack에 넣고 top 을 +1한다
                stack.append(i)
                top += 1
            elif i == ')':              # 소괄호 닫는게 들어온다면

                while stack[top] != '(':    # 짝이 맞는 소괄호 여는게 나올때까지 stack.pop() 값을 더한다
                    if stack[top] != '{' and stack[top] != '}' and stack[top] != ')':
                        result += stack.pop()
                        top -= 1
                    else:           # 만약 괄호가 나오게 된다면 규칙 위배
                        result = -1
                        break
                stack.pop()     # 정상적인 규칙이라면 값을 다 더하고 stack에서 '('를 제거해준다
                top -= 1

            elif i == '}':      # 중괄호 닫는게 들어온다면
                while stack[top] != '{':    # 짝이 맞는 중괄호 닫는게 나올때까지 stack.pop() 값을 곱한다.
                    if stack[top] != '(' and stack[top] != '}' and stack[top] != ')':
                        if result != 0:
                            result *= stack.pop()
                        else:
                            result = stack.pop()
                        top -= 1
                    else:           # 만약 규칙에 맞지 않는 괄호가 나온다면 종료
                        result = -1
                        break
                stack.pop()     # 정상적인 규칙이라면 값을 다 곱하고 stack 에서 '{' 를 제거해준다
                top -= 1

            else:
                stack.append(int(i))       # 문자열로 지정된 숫자가 나온다면 int로 변환하여 stack에 넣어준다
                top +=1

        else:
            if i == '(' or i == '{':              # stack 처음에는 여는 괄호만 가능하다
                stack.append(i)
                top += 1
            else:
                result = -1

    if len(stack) != 0:     # 모든 문자열을 탐색한 후 stack에 무엇인가 남아있다면 규칙 위배
        result =(-1)

    print(f'#{tc} {result}')



