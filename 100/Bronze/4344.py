C = int(input())
for tc in range(1, C+1):
    arr = list(map(int, input().split()))
    # print(arr)
    num =arr.pop(0)
    # print(num)
    # print(arr)
    average = sum(arr)/num
    scores = []
    for i in arr:
        if i > average:
            scores.append(i)

    print(f"{round(len(scores) / num * 100, 3):.3f}%")
