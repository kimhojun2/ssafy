A, B = map(str, input().split())

alpha = []

for a in A:
    for b in B:
        if a == b:
            alpha.append(A.index(a))
            alpha.append(B.index(b))
            break

arr = [['.']*len(A) for _ in range(len(B))]

for i in range(len(B)):
    if i == alpha[1]:
        for j in range(len(A)):
            arr[i][j] =A[j]
for k in range(len(A)):
    if k == alpha[0]:
        for l in range(len(B)):
            arr[l][k] = B[l]

for row in arr:
    print(*row, sep='')