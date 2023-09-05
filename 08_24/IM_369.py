N = int(input())
def f(N):
    for i in range(1, N+1):
        a = 0
        b = 0
        c = 0
        lst = []
        d = i
        while d != 0:
            lst.append(d%10)
            d //= 10
        a = lst.count(3)
        b = lst.count(6)
        c = lst.count(9)
        e = a+b+c
        if a == 0 and b ==0 and c ==0:
            print(i, end=' ')
        else:
            print('-'*e, end=' ')

f(N)