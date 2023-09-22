T = int(input())

def dfs(month, acc_cost):
    global ans

    if month > 12:
        ans = min(ans, acc_cost)
        return

    if acc_cost > ans:
        return

    dfs(month + 1, acc_cost + (months[month]*cost_day))

    dfs(month + 1, acc_cost + cost_month)

    dfs(month+3, acc_cost + cost_month3)

    dfs(month+12, acc_cost + cost_year)

for tc in range(1, T+1):
    cost_day, cost_month, cost_month3, cost_year = map(int, input().split())

    months = [0] + list(map(int, input().split()))
    ans = 100000000000

    dfs(1,0)
    print(f'#{tc} {ans}')