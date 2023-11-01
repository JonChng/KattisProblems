books = int(input())

prices = []

for i in range(books):
    prices.append(int(input()))


prices.sort()


group = []
price = 0
for i in range(len(prices)):
    group.append(prices.pop())

    if len(group) == 3:
        price += sum(group) - min(group)
        group = []

price += sum(group)

print(price)

