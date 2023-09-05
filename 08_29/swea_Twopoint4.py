N = int(input())
arr = list(map(int, input().split()))
arr.sort()

left = 0
right = N-1

minimum = 2e9-1
ansleft = 0
ansright = 0
while left < right:
    sum = arr[left] + arr[right]
    if sum == 0:
        print(arr[left], arr[right])
        exit()

    if minimum > abs(sum):
        minimum =abs(sum)
        ansleft = left
        ansright = right

    if sum > 0:
        right -= 1
    else:
        left +=1
print(arr[ansleft], arr[ansright])