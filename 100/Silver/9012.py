'''
)(
'''

T = int(input())
for tc in range(1, T+1):
    VPS = list(input())
    result = 'YES'
    while len(VPS) != 0:

        if VPS.count('(') != VPS.count(')'):
            result = 'NO'
            break

        elif VPS[0] != '(' or VPS[-1] != ')':
            result = 'NO'
            break

        VPS.remove(VPS[0])
        VPS.remove(VPS[-1])

    print(result)