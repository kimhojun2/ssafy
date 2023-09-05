'''
중위 표기법에서 후위 표기법으로의 변환 알고리즘(스택 이용)2
1. 입력 받은 중위 표기식에서 토큰을 읽는다.
2. 토큰이 피연산자이면 토큰을 출력한다
3. 토큰이 연산자(괄호포함)일 때, 이 토큰이 스택의 top에 저장되어 있는 연산자보다
우선순위가 높으면 스택에 push하고, 그렇지 않다면 스택 top의 연산자의 우선순위가
토큰의 우선순위보다 작을 때까지 스택에서 pop한 후 토큰의 연산자를 push한다.
만약 top에 연산자가 없다면 push한다.
4. 토큰이 오른쪽 괄호')'이면 스택 top에 왼쪽 괄호'('가 올 때까지 스택에 pop연산을 수행하고
pop한 연산자를 출력한다. 왼쪽 괄호를 만나면 pop만 하고 출력하지는 않는다.
5. 중위 표기식에 더 읽을 것이 없다면 중지하고, 더 읽을 것이 있다면 1부터 다시 반복한다.
6. 스택에 남아 있는 연산자를 모두 pop하여 출력한다.
'''


'''
6528-*2/+
'''

stack = [0]*100
top = -1
susik = '6528-*2/+'
for x in susik:
    if x not in '+-/*': # 피연산자면...
        top += 1
        stack[top] = int(x)
    else:
        op1 = stack[top]
        top -= 1
        op2 = stack[top]
        top -= 1

        if x == '+':
            top += 1
            stack[top] = op1 + op2
        elif x =='-':
            top += 1
            stack[top] = op2 - op1
        elif x =='/':
            top += 1
            stack[top] = op2 / op1
        elif x =='*':
            top += 1
            stack[top] = op1 * op2

print(stack[top])