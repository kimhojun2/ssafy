pay = int(input())
coin = [500, 100, 40, 10]

total = 0
cnt = 0
while total != pay:
    if pay - total > 500:
        total += 500
        cnt += 1
    elif pay - total > 100:
        total += 100
        cnt += 1
    elif pay - total > 50:
        total += 50
        cnt += 1
    else:
        total += 10
        cnt += 1
print(cnt)