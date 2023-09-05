from collections import Counter

T = int(input())
for tc in range(1, T+1):
    f = list(map(str, input()))
    text = Counter(input())
    max_cnt = 0
    for i in f:
        if max_cnt < text[i]:
            max_cnt = text[i]
    print(f'#{tc} {max_cnt}')
