# import sys
#
# input = sys.stdin.readline
#
# N = int(input())
# n = sorted(list(map(int, input().split())))
# a = []
# b = []
# for i in n:
#     if i < 0:
#         a.append(i)
#     else:
#         b.append(i)
#
# M = int(input())
# m = list(map(int, input().split()))
# a.sort()
# b.sort()
# # print(n,a,b,m)
#
#
# for card in m:
#     if card < 0:
#         cnt = 0
#         start = 0
#         end = len(a)-1
#         while end >= start:
#             middle = (start + end)//2
#
#             if n[middle] == card:
#                 cnt += a.count(card)
#                 break
#             elif a[middle] > card:
#                 end = middle - 1
#             else:
#                 start = middle + 1
#         print(cnt, end = ' ')
#
#     else:
#         cnt = 0
#         start = 0
#         end = len(b) - 1
#         while end >= start:
#             middle = (start + end) // 2
#
#             if b[middle] == card:
#                 cnt += b.count(card)
#                 break
#             elif b[middle] > card:
#                 end = middle - 1
#             else:
#                 start = middle + 1
#         print(cnt, end=' ')

# import sys
#
# input = sys.stdin.readline
#
# N = int(input())
# n = sorted(list(map(int, input().split())))
# M = int(input())
# m = list(map(int, input().split()))
#
#
# for card in m:
#     cnt = 0
#     start = 0
#     end = len(n)-1
#     while end >= start:
#         middle = (start + end)//2
#
#         if n[middle] == card:
#             cnt += n.count(card)
#             break
#         elif n[middle] > card:
#             end = middle - 1
#         else:
#             start = middle + 1
#     print(cnt, end = ' ')





from collections import Counter
import sys
# 입력받을 n 개의 숫자 카드
n = int(sys.stdin.readline())
# 입력 받은 숫자카드의 숫자를 담은 list
a = Counter(map(int,sys.stdin.readline().split()))
# 숫자카드 확인 횟수
m= int(sys.stdin.readline())
# 확인할 숫자카드 리스트
b = list(map(int,sys.stdin.readline().split()))
# print(a,b)

for i in b:
    # print(i, end = ' ')
    print(0, a[i], end = ' ')

# dic = dict()
# for i in a:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1
#
# for i in range(m):
#     if b[i] in dic:
#         print(dic[b[i]], end= ' ')
#     else:
#         print(0, end=' ')