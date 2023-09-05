import sys
input = sys.stdin.readline

switch = int(input().rstrip())
light =[-1] + list(map(int, input().split()))

k = 1
n = int(input().rstrip())
for i in range(n):
    sex, numb = map(int,input().split())
    #남자 일때는 numb의 배수만큼 light의 스위치를 바꿔줌
    if sex == 1:
        for j in range(1, switch+1):# range(switch) - x , range(1, switch+1) - o
            if j%numb == 0:
                light[j] = abs(light[j]-1)
    else:
    #여자일때
        # 지정된 스위치는 무조건 변경임으로 바로 변경
        light[numb] = abs(light[numb]-1)

        k=1 # 루프 들어기 전 k 초기화 필요
        while True:
            if numb+k>switch or numb-k<1:
                # 벗어나면 종료
                break

            # 둘이 같은지 확인
            if light[numb+k] != light[numb-k]:
                #다르다면 종료
                break

            #같다면 교환
            light[numb+k] = light[numb-k]=abs(light[numb+k]-1)
            k += 1

# 출력 시 문자열에 저장 후 한번에 출력하면 빠름
result = ""
for i in range(1, switch+1):
    if i!=1 and i%20==1:
        result+="\n"
    result+=f"{light[i]} "

print(result)