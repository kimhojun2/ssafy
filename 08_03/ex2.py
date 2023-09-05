board = [int(num) for _ in range(5)]
call = [list(m for _ in range(5)]


d1_st2 = [0] * 10
for n in call:
    # 부른 숫자의 인덱스 찾기
    a = board.index(n)
    # 인덱스를 이용해 해당 숫자의 위치 x, y, 계산
    x, y = a//5, a % 5
    # 가로, 세로, 대각선 빙고 개수 카운트 증가
    x_lst[x] += 1
