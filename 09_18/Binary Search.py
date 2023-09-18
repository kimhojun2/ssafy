# arr = [2,4,7,9,11,19,23]
#
# arr.sort()
#
# def binarySearch(target):
#     low = 0
#     high = len(arr) - 1
#
#     while low <= high:
#         mid = (low+high) // 2
#
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low =mid +1
#         else:
#             high =mid -1
#
#     return "해당 데이터는 없습니다"
#
# print(f"9 = {binarySearch(9)}")
# print(f"4 = {binarySearch(4)}")
# print(f"10 = {binarySearch(10)}")

#재귀호출
arr = [2,4,7,9,11,19,23]
arr.sort()
# 함수 한 번 호출 때 마다 low, high 변수가 바뀌어서 사용됨
def binarySearch(low, high, target):
    if low > high:
        return -1

    mid = (low + high)//2

    if target == arr[mid]:
        return mid

    elif arr[mid] < target:
        return binarySearch(mid+1, high, target)

    else:
        return binarySearch(low, mid-1, target)

print(f"9 = {binarySearch(0, len(arr) - 1, 9)}")
print(f"4 = {binarySearch(0, len(arr)-1 , 4)}")
print(f"10 = {binarySearch(0, len(arr)-1, 10)}")