# def shooting(balloon):
#     cnt = 0
#
#     while len(balloon) != 0:
#         if len(balloon) != 1:
#             max_score = 0
#             B = [0]
#             for b in range(len(balloon)):
#                 score = 0
#                 if max(balloon) != balloon[b]:
#                     if b == 0:
#                         score = 1*balloon[1]
#                     elif b == len(balloon) -1:
#                         score = 1*balloon[-2]
#                     else:
#                         score = balloon[b-1]*balloon[b+1]
#
#                 if score > max_score:
#                     max_score = score
#                     B[0] = b
#
#                 elif score == max_score:
#                     if B[0] > b:
#                         B[0] = b
#             cnt += max_score
#             balloon.pop(B[0])
#         else:
#             cnt += balloon[0]
#             balloon.pop()
#
#     return cnt
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     balloon = list(map(int, input().split()))
#     print(shooting(balloon))
def max_balloon_score(nums):
    n = len(nums)
    if n == 1:
        return nums[0]

    max_score = 0
    for i in range(n):
        left_val = nums[i - 1] if i - 1 >= 0 else 1
        right_val = nums[i + 1] if i + 1 < n else 1
        score = left_val * right_val
        new_nums = nums[:i] + nums[i + 1:]
        score += max_balloon_score(new_nums)
        max_score = max(max_score, score)

    return max_score


# 입력 처리 및 결과 출력
T = int(input())  # 테스트 케이스 개수 입력

for case in range(1, T + 1):
    N = int(input())  # 풍선의 개수 입력
    balloon_scores = list(map(int, input().split()))  # 풍선의 점수 입력

    result = max_balloon_score(balloon_scores)  # 최대 점수 계산
    print(f"#{case} {result}")  # 결과 출력
