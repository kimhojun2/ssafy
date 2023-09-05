def func(n):
    if n % 10 ==0:
        if n ==10:
            return 1
        elif n == 20:
            return 3

        else:
            return func(n-10) + (2*func(n-20))

T =  int(input())
for tc in range(1, T+1):
    n = int(input())
    num = func(n)
    print(f'#{tc} {num}')






# T = int(input())
#
# def paper_10(n):
#     if n == 0:
#         return
#     global cnt
#     cnt+=1
#     n -= 10
#     paper_10(n)
#
# def paper_20(n):
#     if n == 0:
#         return
#     global cnt
#     cnt +=1
#     n-=20
#     if 10 <= n <20:
#         paper_10(n)
#     else:
#         paper_20(n)
#
#
#
#
#
# for tc in range(1, T+1):
#     N = int(input())
#     cnt = 0
#     # while N != 0:
#         # if N >= 20:
#         #     N -= paper(20)
#         #     cnt += 1
#         # elif 10<=N<=20:
#         #     N -= paper(10)
#         #     cnt += 1
#     paper_20(N)
#     print(cnt)
#
#
