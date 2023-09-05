T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    answer = list(map(int, input().split()))
    score_lst = []
    for n in range(N):
        student_answer = list(map(int, input().split()))
        score = 0
        cnt = 0
        for i in range(M):
            if answer[i] == student_answer[i]:
                cnt += 1
                score += cnt

            else:
                cnt = 0

        score_lst.append(score)
    print(f'#{tc} {max(score_lst)-min(score_lst)}')
