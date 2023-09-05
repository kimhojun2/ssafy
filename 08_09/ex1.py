arr = [3, 5, 1, 9, 7]

for i in range(4):
    alpha = input()

    if alpha == 'L':
        num_L = arr.pop(0)
        arr.append(num_L)
    else:
        num_R = arr.pop()
        b = list(reversed(arr))
        b.append(num_R)
        arr = list(reversed(b))


print(arr)

'''
R
R
R
L
'''