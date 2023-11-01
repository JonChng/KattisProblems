n, t = map(int, input().split())

timings = list(map(int,input().split()))

total_time = 0
count = 0

for i in timings:
    if total_time + i <= t:
        total_time += i
        count += 1
    else:
        break

print(count)