# '''
# 100+100-50+30
# '''
#
# cal = input()
# i = 0
# lst = []
# while i < len(cal):
#     num = ''
#     if cal[i] == '+':
#         lst.append(int(num))
#         i+=1
#
#     elif cal[i] == '-':
#         lst.append(int(num)*-1)
#         i+=1
#
#     else:
#         num += cal[i]
#         i+=1
# print(lst)

# print(eval(input()))

ex = input()
if ex[0] == '-':
    ex = '0' + ex

word = ex.split('+')
ans = 0
for w in word:
    w = w.split('-')
    inner_ans = int(w[0])

    for i in range(1, len(w)):
        inner_ans -= int(w[i])
    ans += inner_ans
print(ans)