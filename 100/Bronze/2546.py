T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    c_score = list(map(int, input().split()))
    e_score = list(map(int, input().split()))
    count = 0
    for c in c_score:
        if c < sum(c_score)/len(c_score):
            if c> sum(e_score)/len(e_score):
                count += 1

    print(count)