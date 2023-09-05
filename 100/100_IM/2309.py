# 일곱 난쟁이
nan = []
for i in range(9):
    nan.append(int(input()))
def f():
    result = 1
    fn1 =0
    fn2 = 0
    for a in range(8):
        for b in range(a+1,9):
            if sum(nan) - nan[a] - nan[b] == 100:
                fn1 = nan[a]
                fn2 = nan[b]
                result = 0
                break
        if result == 0:
            break
    nan.remove(fn1)
    nan.remove(fn2)
f()
for n in sorted(nan):
    print(n)

