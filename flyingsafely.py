n = int(input())

for i in range(n):

    cities, pilots = map(int, input().split())

    if pilots < cities:
        ans = pilots

    else:
        ans = cities - 1


    routes = []
    for j in range(pilots):
        destinations = list(map(int, input().split()))
    print(cities - 1)

