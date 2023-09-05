K = int(input())
money = []
for k in range(K):
    N = int(input())
    if N != 0:
        money.append(N)
    else:
        money.pop()
print(sum(money))