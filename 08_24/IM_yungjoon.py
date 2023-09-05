T = int(input())
for tc in range(1, T+1):
    cards = input()
    S = 13
    D = 13
    H = 13
    C = 13
    stack = []
    result = 0
    for i in range(len(cards)//3):
        num = cards[i*3:i*3+3]
        if num not in stack:
            stack.append(num)
        else:
            print(f'#{tc} ERROR')
            result = 1
            break

    if result == 0:
        for j in range(len(stack)):
            if 'S' in stack[j]:
                S -=1
            elif 'D' in stack[j]:
                D -= 1
            elif 'H' in stack[j]:
                H -= 1
            else:
                C -= 1
        print(f'#{tc} {S} {D} {H} {C}')

