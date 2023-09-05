N = int(input())

def func(N):
    if N//10 >= 1:
        return func(N//10) + func(N%10)
    else:
        return N

print(func(N))