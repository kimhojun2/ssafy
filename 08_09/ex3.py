# 콜라츠 추측

def func(N):
    if N != 1:
        if N%2==0:
            return func(N//2) + 1
        else:
            return func(N*3 + 1) +1
    else:
        return 0

N = int(input())
print(func(N))