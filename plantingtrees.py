trees = int(input())

all_trees = list(map(int, input().split()))

all_trees.sort(reverse=True)

days = []

for i in range(len(all_trees)):
    day = (i + 1) + all_trees[i] + 1
    days.append(day)

print(max(days))