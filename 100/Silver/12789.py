N = int(input())
numbers = list(map(int, input().split()))
# side = []
result = 'Nice'
order = 1
def ddd(numbers,order):
    side = []
    result = 'Nice'
    for num in numbers:
        side.append(num)

        while side != []:
            if side[-1] == order:
                side.pop()
                order += 1

            else:
                break
        # print(side)
    if len(side) != 0:
        result = 'Sad'
    return result
print(ddd(numbers,order))


# N = int(input())
# arr = list(map(int, input().split()))
#
#
#
# def lineup(N, arr):
#     stack = []
#     cnt = 1                          # cnt 는 지금 간식을 받으러 와야하는 번호를 의미 -> 시작 1번부터
#     for i in range(N):                   # 리스트 순회
#         if arr[i] != cnt:                 # 현재 인덱스에서 해당 번호가 cnt와 다른경우
#             if len(stack) > 0:               # stack 은 줄 정리 공간 stack에 사람이 있는경우
#                 if stack[-1] == cnt:          # stack의 가장 위에 있는 번호가 cnt와 일치할경우
#                     cnt += 1
#                     stack.pop()               # 간식을 받고 스택 pop , cnt ++
#                     for k in range(len(stack)):        # 남아있는 스택을 순회
#                         if stack[-1] == cnt:
#                             cnt += 1
#                             stack.pop()                # 남아있는 스택에서 다음 번호에 해당하는 사람이 올라와있다면 간식 수령
#
#                         else:
#                             stack.append(arr[i])       # 아니라면 현재 인덱스 i의 번호를 스택에 넣는다
#                     break
#                 else:
#                     stack.append(arr[i])               # 스택에 해당 번호가 나와있지 않다면 그위에 현재 인덱스값 추가
#             else:
#                 stack.append(arr[i])                #  스택이 비어있을 경우 i를 바로 스택에 넣음
#
#         else:
#             cnt += 1                    # arr[i]가 현재 간식 번호라면 간식받고 cnt ++
#
# # 한차례 arr 순회가 끝나면 스택에만 사람이 남아있을 것. 혹은 다 비어져 있거나
#
#     for j in range(len(stack)):                  # 스택을 순회
#         num = stack.pop()                          # 하나씩 뽑아서
#         if num == cnt:                             # 자기 차례면 간식받음
#             cnt += 1
#         else:
#             return 'Sad'                           # 한번이라도 cnt 가 아닌데 스택에서 나온다면 sad
#
#
#     return 'Nice'                                 # 성공적으로 다 돌았으면 나이스
#
#
# print(lineup(N, arr))



