# # 주사위 쌓기
# # (0, 5)(1, 3)(2, 4)
# def f(N, dice):
#     global MAX
#     global top_side
#     global bottom_side
#     nums = [1, 2, 3, 4, 5, 6]
#     if top_side == 0 and bottom_side == 0:
#         for nn in range(6):
#             bottom = dice[nn]
#             top = dice[5 - nn]
#             nums.remove(bottom)
#             nums.remove(top)
#             max_side = max(nums)
#             if max_side > MAX:
#                 MAX = max_side
#                 top_side = top
#                 bottom_side = bottom
#     else:
#         bottom = top_side
#         top = dice[5 - dice.index(bottom)]
#         nums.remove(bottom)
#         nums.remove(top)
#         MAX += max(nums)
#         top_side = top
#         bottom_side = bottom

# N = int(input())
# MAX = 0
# top_side = 7
# bottom_side = 7
# for n in range(N):
#     dice = list(map(int, input().split()))
#     nums = [1, 2, 3, 4, 5, 6]
#     if n == 0:
#         for nn in range(5):
#             numbers = [1,2,3,4,5,6]
#             bottom = dice[nn]
#             top = dice[5-nn]
#             numbers.remove(bottom)
#             numbers.remove(top)
#             max_side = max(numbers)
#             if max_side >= MAX:
#                 MAX = max_side
#                 if top < top_side:
#                     bottom_side = bottom
#                     top_side = top
#     else:
#         bottom = top_side
#         top = dice[5-dice.index(bottom)]
#         nums.remove(bottom)
#         nums.remove(top)
#         MAX += max(nums)
#         top_side = top
#         bottom_side = bottom
#     # f(N, dice)
# print(MAX)
N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]

def max_num():
    result = []
    for i in range(6):
        sum = 0
        start = arr[0][i]
        for j in range(N):
            list1 = []
            index = arr[j].index(start)
            list1.append(start)
            if index == 0 or index == 5:
                start = arr[j][5-index]
                list1.append(start)
            elif index == 1 or index == 3:
                start = arr[j][4-index]
                list1.append(start)
            elif index == 2 or index == 4:
                start = arr[j][6-index]
                list1.append(start)
            complement = list(set(arr[j]) - set(list1))
            sum += max(complement)
        result.append(sum)
    result.sort()
    return result[-1]

print(max_num())