# # # T = int(input())
# # # for tc in range(1, T+1):
# # #     N = int(input())
# # #     arr = list(map(int, input().split()))
# # #
# # #     for i in range(N-1, 0, -1):  #i 구간의 마지막 인덱스
# # #         for j in range(i):
# # #             if arr[j] > arr[j+1]:
# # #                 arr[j], arr[j+1] = arr[j+1], arr[j]
# # #
# # #     print(f'#{tc}', *arr)
# #
# # numbers = [4, 1, 2, 3, 5]
# # def bublle(arr):
# #     for i in range(len(arr)):
# #         for j in range(len(arr)-i-1):
# #             if arr[j] > arr[j+1]:
# #                 arr[j], arr[j+1] = arr[j+1], arr[j]
# #
# # bublle(numbers)
# # print(numbers)
# list1 = [1,4,1,2,7,5,2]
# def counting(arr):
#     max_value = max(arr)
#     count_arr = [0]*(max_value + 1)
#
#     for num in arr:
#         count_arr[num] += 1
#     sorted_arr = []
#     for i, count in enumerate(count_arr):
#         sorted_arr.extend([i]*count)
#     return sorted_arr
#
# list1 = [1,4,1,2,7,5,2]
# sorted_list = counting(list1)
# print(sorted_list)

def greedy(money, coins):
    coins.sort(reverse = True)
    change = {coin : 0 for coin in coins}
    for coin in coins:
        while money >= coin:
            money -= coin
            change[coin] += 1
    return change
result = greedy(380, [100,50,10])
print(result)