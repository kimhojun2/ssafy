# #2진수 만들기
#
# def function(N):
#     if N//2 > 1:
#         return function(N//2) + '1'
#
#     elif N%2 == 1:
#         return '1'
#     else:
#         return '0'
# N = int(input())
# print(function(N))


def func(n):
    if n ==0:
        return '0'
    elif n ==1:
        return '1'
    else:
        return func(n//2) +str(n % 2)
N = int(input())
print(func(N))