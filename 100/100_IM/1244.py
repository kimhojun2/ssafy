N = int(input())
switch = list(map(int, input().split()))
S = int(input())
student = []
for s in range(S):
    num = list(map(int, input().split()))
    student.append(num)

for i in student:
    if i[0] == 1:
        a = i[1]
        h = 1
        while a <= len(switch):
            if switch[a-1] == 0:
                switch[a-1] = 1
            else:
                switch[a-1] = 0
            a //= h
            h += 1
            a *= h

    else:
        if i[1] != len(switch) and i[1] != 1:
            left = list(reversed(switch[:i[1]-1]))
            right = switch[i[1]:]

            u = 0
            while left[u] == right[u]:
                u += 1
                if u == len(left) or u == len(right):
                    break
            g = switch[i[1]-1]
            if g == 0:
                g = 1
            else:
                g = 0

            if u != 0:
                for v in range(u):
                    if left[v] == 0:
                        left[v] = 1
                    else:
                        left[v] = 0

                    if right[v] == 0:
                        right[v] = 1
                    else:
                        right[v] = 0

            switch = list(reversed(left))
            switch.append(g)
            switch.extend(right)
        else:
            if switch[i[1]-1] == 0:
                switch[i[1]-1] = 1
            else:
                switch[i[1]-1] = 0

fff = len(switch)//20
if fff > 0:
    idx = 0
    for i in range(fff):
        print(*switch[i: i+20])
        idx += 1
    print(*switch[idx*20:])
else:
    print(*switch)