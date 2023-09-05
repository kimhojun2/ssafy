T = int(input())
for tc in range(1, T+1):
    info = input()
    stack = []
    cnt = 0
    count =0
    for i in info:
        if len(stack) == 0:
            stack.append(i)

        else:
            if i == ')':
                if stack[-1] == '(':
                    stack.pop()
                    cnt += len(stack)

                else:
                    stack.pop()

            else:
                stack.append(i)
        print(stack, cnt)
    print(cnt)






'''
cnt+1           ( 다음 ( 오면 이전 (이거는 무조건 막대기         
(cnt-1)/2       ( 다음 ) 오면 이전 (는 막대기 아니고 레이저
cnt -1          ) 다음 )이거 오면 막대기 닫기
'''