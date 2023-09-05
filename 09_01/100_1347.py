from collections import deque
N = int(input())
MAP = list(input())
# print(MAP)
arr = [['.']]
cnt = 0
i = 0
j = 0
for m in MAP:
    if m == 'F':
        if cnt <= 0 :
            d = abs(cnt)
            if d % 4 == 0:
                arr.append(['.'])
                i += 1
            elif d % 4 == 1:
                arr[i].append('.')
                j += 1
            elif d % 4 == 2:
                arr.append(['.'])
                if i != 0:
                    i -= 1
            else:
                arr[i].append('.')
                if j != 0:
                    j -= 1

        else:
            d = cnt

            if d%4 == 0:
                arr.append(['.'])
                i+=1
            elif d%4 == 1:
                arr[i].append('.')
                if j != 0:
                    j -= 1
            elif d%4 == 2:
                arr.append(['.'])
                if i != 0:
                    i -= 1
            else:
                arr[i].append('.')
                j += 1

    elif m == 'R':
        cnt += 1

    else:
        cnt -= 1

print(arr)