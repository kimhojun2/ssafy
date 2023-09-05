# # 수열
# N, K = map(int, input().split())
# weather = list(map(int, input().split()))
#
# max_weather = -10e23
# i = 0
# while True:
#     if i + K <= N:
#         lst = weather[i:i+K]
#         sum_weather = sum(lst)
#         if sum_weather > max_weather:
#             max_weather = sum_weather
#     else:
#         break
#
#     i += 1
#
# print(max_weather)

N, K = map(int, input().split())    # N: 날짜의수, K: 연속적인 날짜의 수
arr = list(map(int, input().split()))   # 측정한 온도 / N일 만큼
result = []
result.append(sum(arr[:K]))

for i in range(N - K):
    result.append(result[i] - arr[i] + arr[i + K])

print(max(result))