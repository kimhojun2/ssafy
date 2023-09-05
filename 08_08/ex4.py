'''
2025.X.1X
'''
Y, M, D = map(str, input().split('.'))


def year(Y):
    cnt_y = 0
    if Y.count('X') == 4:
        cnt_y += 1
    elif Y.count('X') == 3 or Y.count('X') == 2 or Y.count('X') == 1:
        if Y[0] != 'X':
            cnt_y += 10**Y.count('X')
        else:
            cnt_y += 9*(10**(Y.count('X')-1))
    else:
        cnt_y +=1

    return cnt_y


def month(M):
    cnt_m = 0
    if M.count('X') == 2:
        cnt_m +=3
    elif M.count('X') == 1:
        if M[0] == 'X' and len(M) == 2:
            cnt_m +=1
        else:
            cnt_m += 9
    else:
        cnt_m += 1

    return cnt_m


def day(D):
    cnt_d = 0
    if D.count('X') == 2:
        cnt_d += 22
    elif D.count('X') == 1:
        if D[0] == 'X':
            if D[1] == '1' or D[1] == '0':
                cnt_d += 3
            else:
                cnt_d += 2

        elif D[1] == 'X':
            if D[0] == '3':
                cnt_d += 2
            else:
                cnt_d +=10
    else:
        cnt_d += 1

    return cnt_d


y = year(Y)
m = month(M)
d = day(D)

print(y*m*d)