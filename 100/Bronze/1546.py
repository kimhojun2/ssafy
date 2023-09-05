N = int(input())
scores = list(map(int, input().split()))

M = max(scores)
new_scores = []
for score in scores:
    new_scores.append(score/M*100)

average_score = sum(new_scores)/N

print(average_score)