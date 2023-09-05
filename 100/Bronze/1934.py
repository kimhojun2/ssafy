T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    for i in range(min(A,B),0,-1):
        if A%i==0 and B%i==0:
            print((A*B)//i)
            break