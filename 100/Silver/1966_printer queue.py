from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    queue = deque(map(int, input().split()))
    idx = deque()
    for index, value in enumerate(queue):
        idx.append((value, index))
    cnt = 0
    while len(idx) != 0:
        a = idx.popleft()
        if len(idx) != 0:
            if a[0] < max(item[0] for item in idx):
                idx.append(a)
            else:
                cnt += 1
                if a[1] == M:
                    print(cnt)
                    break
        else:
            cnt += 1
            print(cnt)
            break

