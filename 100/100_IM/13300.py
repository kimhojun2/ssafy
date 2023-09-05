# 방배정
def room(K, S, Y):
    global cnt
    if S == 0:
        if room_0[Y] == 0:
            cnt += 1
            room_0[Y] += 1
        elif 0 < room_0[Y] <K:
            room_0[Y] += 1
        else:
            room_0[Y] = 1
            cnt += 1

    else:
        if room_1[Y] == 0:
            cnt += 1
            room_1[Y] += 1
        elif 0 < room_1[Y] < K:
            room_1[Y] += 1
        else:
            room_1[Y] = 1
            cnt += 1
    return cnt
N, K = map(int, input().split())
room_0 = [0]*7
room_1 = [0]*7
cnt = 0
for n in range(N):
    S, Y = map(int, input().split())
    room(K, S, Y)

print(cnt)
