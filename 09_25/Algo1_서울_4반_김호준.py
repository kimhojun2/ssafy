T = int(input())
for tc in range(1, T+1):
    N = int(input())
    code = input()
    key = input()
    keys = {
        'A': 11,
        'B': 12,
        'C': 13,
        'D': 14,
        'E': 15,
        'F': 16,
        11 : 'A',
        12: 'B',
        13: 'C',
        14: 'D',
        15: 'E',
        16: 'F',
    }
    if key.isdigit() == True:   # key 값이 0~9 까지인지 아닌지 확인
        key = int(key)
    else:
        key = keys[key]

    ans = ''
    for c in range(N):
        if key == 1:        # key 값이 0이라면 코드값을 그대로 반환
            ans += code[c]
            continue

        if code[c].isdigit() == True:   # code 값이 0~9 까지인지 아닌지 확인
            C = int(code[c])
        else:
            C = keys[code[c]]

        if C == 0:              # Code 값이 0이라면
            if key > 10:
                ans += keys[key]
            else:
                ans += str(C)
            continue
        if C == key:        # key 와 code가 같다면
            ans += '0'
            continue
        if C < key:
            if key + C <= 16:
                if key + C > 10:
                    ans += keys[key + C]
                else:
                    ans += str(key+C)
            else:
                ans += str(abs(C+1 - key))
            continue

        if C > key:
            if C - key > 10 :
                ans += keys[C -key]
            else:
                ans += str(C - key)



    print(f'#{tc} {ans}')
