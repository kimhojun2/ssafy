# def fff(S):
#     stack = []
#     result = True
#     for s in S:
#         if s == '.':
#             break
#
#         elif len(stack) >= 2:
#             if s not in '+-*/':
#                 stack.append(int(s))
#             else:
#                 s2 = stack.pop()
#                 s1 = stack.pop()
#
#                 if s == '+':
#                     stack.append(s1 + s2)
#
#                 elif s == '-':
#                     stack.append(s1 - s2)
#
#                 elif s == '/':
#                     stack.append(s1 // s2)
#
#                 elif s == '*':
#                     stack.append(s1 * s2)
#
#         else:
#             if s not in '+-*/':
#                 stack.append(int(s))
#             else:
#                 result = False
#                 break
#     return result
'''
T = int(input())
for tc in range(1, T+1):
    S = list(map(str, input().split()))
    # fff(S)
    stack = []
    result = True
    for s in S:
        if s == '.':
            break

        elif len(stack) >= 2:
            if s not in '+-*/':
                stack.append(int(s))
            else:
                s2 = stack.pop()
                s1 = stack.pop()

                if s == '+':
                    stack.append(s1 + s2)

                elif s == '-':
                    stack.append(s1 - s2)

                elif s == '/':
                    stack.append(s1 // s2)

                elif s == '*':
                    stack.append(s1 * s2)

        else:
            if s not in '+-*/':
                stack.append(int(s))
            else:
                result = False
                break

    if result == True and len(stack) == 1:
        print(f'#{tc} {stack[0]}')
    else:
        print(f'#{tc} error')
'''
# 강사님 코드

# T = int(input())
# for tc in range(1, T+1):
#     forth = list(input())
#     stack = []
#     error = False
#     for i in range(len(forth)-1):
#         if forth[i].isdigit():      # 문자열이 숫자인지 판별!!!!!
#             stack.append(forth[i])
#         else:
#             try:
#                 b = int(stack.pop())
#                 a = int(stack.pop())
#                 if forth[i] == '+':
#                     ans = a + b
#                 elif forth[i] == '-':
#                     ans = a - b
#                 elif forth[i] == '*':
#                     ans = a * b
#                 elif forth[i] == '/':
#                     ans = a // b
#                 stack.append(ans)
#             except: # 두개의 숫자를 꺼낼 수 없는 경우
#                 error = True
#
#     if error == True or len(stack) != 1:
#         print(f'#{tc} error')
#
#     else:
#         print(f'#{tc} {stack.pop()}')

