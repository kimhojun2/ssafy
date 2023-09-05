'''
슬라이딩 윈도우
input
10 2
3 -2 -4 -9 0 3 7 13 8 -3
output
21
'''
# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# sum = 0
# for i in range(m):
#     sum += arr[i]
#     Max = sum
#
# for j in range(n-m):
#     sum += arr[j+m]
#     sum -= arr[j]
#     if sum > Max:
#         Max = sum
#
# print(Max)
'''
투 포인터
input
10 5
1 2 3 4 2 5 3 1 1 2
output
3
'''
# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# cnt, sum = 0, 0
# high, low = 0, 0
# while True:
#     if sum >= m or high == n:
#         sum -= arr[low]
#         low +=1
#     elif sum < m:
#         sum += arr[high]
#         high +=1
#     if sum == m:
#         cnt +=1
#     if low == n:
#         break
# print(cnt)

'''
데이터 값 정리
arr는 메모리를 많이 잡아먹는다

arr =[
    [0, 0, 1, 0]
    [0, 0, 1, 0]
    [1, 1, 0, 1]
    [0, 0, 1, 0]
]
graph = {
    0: [2]
    1: [2]
    2: [0, 1, 3]
    3: [2]
}
INDEX = [(2, 0), (2, 1), (2, 3)]

'''
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    sum = 0
    x = 0
    y = 0
    for i in range(m):
        sum += arr[i]
        Max = sum
        x = 0
        y = i


    for j in range(n-m):
        sum += arr[j+m]
        sum -= arr[j]
        if sum > Max:
            Max = sum
            y = j+m
            x = j+1

    print(f'#{tc} {x} {y} {Max}')