A, B, V = map(int, input().split())
Day = (V-A)//(A-B) + 1
if (V-A)%(A-B) != 0:
    Day +=1
print(int(Day))