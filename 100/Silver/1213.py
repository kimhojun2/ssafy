S = input()
stack = []
a = sorted(S)
idx = 0
word = []
while idx < len(a):
    if len(stack) == 0:
        stack.append(a[idx])
        idx += 1
    else:
        if stack[-1] == a[idx]:
            b = stack.pop()
            word.append(b)
            idx += 1

        else:
            stack.append(a[idx])
            idx +=1

# print(stack)
# print(word)

if len(stack) > 1:
    print("I'm Sorry Hansoo")
elif len(stack) == 1:
    print(''.join(word), end = '')
    print(stack[0], end='')
    print(''.join(reversed(word)))

else:
    print(''.join(word), end='')
    print(''.join(reversed(word)))