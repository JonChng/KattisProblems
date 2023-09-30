cases = int(input())

for i in range(cases):
    stops = int(input())

    count = 0

    for j in range(stops):
        count += 0.5
        count = count * 2

    print(int(count))


