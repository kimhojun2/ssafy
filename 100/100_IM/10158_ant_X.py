# 가로 w 세로 h  (0,0) ,(w,h)
# 개미의 좌표 (p,q)
# t 시간 후의 x,y 의 좌표
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
a = (p + t) // w  # 반복된 횟수를 구해 홀수면 -1 중, 짝수면 +1 중
b = (q + t) // h  # w,h 값 만큼 도달하지 못했을땐 나눠도 0 인것을 생각하면 이해됌.

if a % 2 == 0:  # 짝수이면 + 중이기에 남은 값 그대로 반환
    x = (p + t) % w
else:  # 홀수이면 - 중이기에 남은 값을 최댓값에서 빼기
    x = w - (p + t) % w

if b % 2 == 0:
    y = (q + t) % h
else:
    y = h - (q + t) % h

print(x, y)