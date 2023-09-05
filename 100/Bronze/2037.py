p, w =map(int,input().split())
letters = list(input())
print(letters)
asc = []
for letter in letters:
    if ord(letter) > 64:
        asc.append(ord(letter)-64)
    else:
        asc.append(ord(letter)-32)
print(asc)

time = 0
for i in range(0, len(asc)):
    if i == len(asc):
        if asc[i]


    elif asc[i] == 0:
        time += p

    elif 16<=asc[i]<=19:
        if (asc[i]-15)//5 == (asc[i+1]-15)//5:
            time += p*(asc[i]%5) + w
        else:
            time += p*(asc[i]%5)

    elif 23 <= asc[i]:
        if (asc[i]-15)//5 == (asc[i+1]-15)//5:
            time += p*(asc[i]%5) + w
        else:
            time += p*(asc[i]%5)
    else:
        if asc[i]//4 == asc[i+1]//4:
            time += p*(asc[i]%4) + w
        else:
            time += p*(asc[i]%4)

print(time)

#        ['A', 'B', 'C'],   1 2 3
#        ['D', 'E', 'F'],   4 5 6
#        ['G', 'H', 'I'],   7 8 9
#        ['J', 'K', 'L'],   10 11 12
#        ['M', 'N', 'O'],   13 14 15
#        ['P', 'Q', 'R', 'S'],  16 17 18 19
#        ['T', 'U', 'V'],   20 21 22
#        ['W', 'X', 'Y', 'Z']]  23 24 25 26