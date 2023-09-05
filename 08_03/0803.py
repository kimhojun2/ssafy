bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = 1
                print(bit)

# def print_subset(bit, arr, n):
#     total = 0
#     for i in range(n):
#         if bit[1]:
#             print(arr[i], end=" ")
#             total +=arr[i]
#     print(bit, total)
#
# arr = [1, 2, 3, 4]
# bit = [0, 0, 0, 0]

# arr = [3,6,7,1,5,4]
#
# n = len(arr)
#
# for i in range(1<<n):
#     for j in range(n):
#         if i & (1<<j):
#             print(arr[j], end=", ")
#     print()
# print()


# 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고
# 검색을 계속 진행하는 방법


#               이진탐색
# def binarySearch(a, N, key):
#     start = 0
#     end = N-1
#     while start <= end:
#         middle = (start +end)//2
#         if a[middle] == key:
#             return key
#         elif a[middle] > key:
#             end = middle -1
#         else:
#             start = middle + 1


#           선택정렬
# def selectionSort(a, N):
#     for i in range(N-1):
#         minIdx = i
#         for j in range(i+1, N):
#             if a[minIdx] > a[j]:
#                 minIdx = j
#         a[i], a[minIdx] = a[minIdx], a[i]
#         print(a)
# arr = [1,5,6,2,56,11,34,8]
# N= len(arr)
# selectionSort(arr, N)