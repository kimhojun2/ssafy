word = input()
result = 0
for i in range(len(word)):
    temp = ''
    index = i +1
    if word[i] == '[':
        while word[index] != ']':
            temp += word[index]
            index += 1
        result += int(temp)
    elif word[i] == '{':
        while word[index] != '}':
            temp += word[index]
            index += 1
        result *= int(temp)

print(result)