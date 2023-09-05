N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

stack = []
cnt = 1
ans = ''
for j in arr:

    while cnt <= j:
        stack.append(cnt)
        ans += '+'
        cnt += 1

    if stack[-1] == j:
        stack.pop()
        ans += '-'

    else:
        ans += 'N'
        break

for k in ans:
    if ans.find('N') != -1:
        print('NO')
        break
    else:
        print(k)