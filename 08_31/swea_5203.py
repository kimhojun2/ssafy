T = int(input())
for tc in range(1, T+1):
    nums = list(map(int,input().split()))
    A = []
    B = []
    result = 0
    for i in range(len(nums)):
        if i%2 == 0:
            A.append(nums[i])
            if A.count(nums[i]) == 3:
                result = 1
                break
            elif nums[i] - 1 in A and nums[i] - 2 in A:
                result = 1
                break
            elif nums[i] - 1 in A and nums[i] + 1 in A:
                result = 1
                break
            elif nums[i]+1 in A and nums[i] + 2 in A:
                result = 1
                break
        else:
            B.append(nums[i])
            if B.count(nums[i]) == 3:
                result = 2
                break
            elif nums[i] - 1 in B and nums[i] - 2 in B:
                result = 2
                break
            elif nums[i] - 1 in B and nums[i] + 1 in B:
                result = 2
                break
            elif nums[i]+1 in B and nums[i] + 2 in B:
                result = 2
                break
    print(f'#{tc} {result}')