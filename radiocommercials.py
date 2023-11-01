
breaks, cost = map(int, input().split())
views = list(map(int, input().split()))

max_profit = 0
current_profit = 0

for view in views:
    current_profit += view - cost

    if current_profit < 0:
        current_profit = 0

    if current_profit > max_profit:
        max_profit = current_profit

print(max_profit)

