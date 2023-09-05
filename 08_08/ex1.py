# criminal = list(map(str, input()))
# c = []
# for i in criminal:
#     if 48 <= ord(i) <= 57:
#         c.append(int(i))
#     else:
#         c.append(i)
#
# k = 0
# j = 0
# while k < len(c):
#
#     alpha = ''
#     num = []
#
#     while j < len(c):
#
#         if type(c[j]) == str:
#             alpha += c[j]
#             j +=1
#         else:
#             num.append(c[j])
#             if j+1 != len(c):
#                 if type(c[j+1]) == str:
#                     j += 1
#                     total = 17
#                     for z in range(0, len(num)):
#                         total += num[z] * (10 ** abs(z - len(num) + 1))
#                     print(f'{alpha}#{total}')
#                     break
#
#                 else:
#                     j += 1
#             else:
#                 j += 1
#                 total = 17
#                 for z in range(0, len(num)):
#                     total += num[z] * (10 ** abs(z - len(num) + 1))
#                 print(f'{alpha}#{total}')
#                 break
#
#         k = j
#
#

criminal = input()
c = []
for i in criminal:
    if 48 <= ord(i) <= 57:
        c.append(int(i))
    else:
        c.append(i)

X = True
j = 0
while X :

    alpha = ''
    num = []

    while j < len(c):

        if type(c[j]) == str:
            alpha += c[j]
            j +=1
        else:
            num.append(c[j])
            if j+1 != len(c):
                if type(c[j+1]) == str:
                    j += 1
                    total = 17
                    for z in range(0, len(num)):
                        total += num[z] * (10 ** abs(z - len(num) + 1))
                    print(f'{alpha}#{total}')
                    break

                else:
                    j += 1
            else:
                j += 1
                total = 17
                for z in range(0, len(num)):
                    total += num[z] * (10 ** abs(z - len(num) + 1))
                print(f'{alpha}#{total}')
                X = False
                break




