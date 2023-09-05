N, M = map(int, input().split())
monster = {}
for n in range(1, N+1):
    a = input()
    monster[n] = a
    monster[a] = n

for m in range(M):
    b = input()
    if b.isdigit() == True:
        print(monster[int(b)])
    else:
        print(monster[b])
