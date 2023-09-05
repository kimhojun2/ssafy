card = list(input())
path = [0] * 4
cnt = 0
def card_cnt(level):
    global cnt
    if level == 4:
        cnt +=1
        return

    for i in range(5):
        path[level] = card[i]
        if int(path[level]) - int(path[level - 1]) >= 4:
            continue
        if int(path[level-1]) - int(path[level]) >= 4:
            continue
        card_cnt(level + 1)

card_cnt(0)
print(cnt)
