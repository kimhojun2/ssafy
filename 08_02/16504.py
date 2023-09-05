T = int(input())

for tc in range(1, T+1):
    #방의 가로길이 입력
    N = int(input())
    arr = list(map(int, input().split()))
    max = 0

    for i in range(N):
        cnt = 0
        # 현재 위치의 오른쪽에 있는 모든 상자를 확인
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                cnt += 1
        # 최대값
        if max <= cnt:
            max = cnt

    print(f'#{tc} {max}')