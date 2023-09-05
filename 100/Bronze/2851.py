mushroom = [int(input())for _ in range(10)]
# print(mushroom)
sum = 0

for i in mushroom:
    sum += i
    if sum > 100:
        old_sum = sum - i
        if abs(sum - 100) <= abs(old_sum-100):
            result = sum
            break
        else:
            result = old_sum
            break
    else:
        result = sum


print(result)