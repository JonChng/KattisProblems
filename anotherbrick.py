h, w, n = map(int, input().split())

bricks = list(map(int, input().split()))

ok = True

count = 0
finished = 0

for i in bricks:
    if count + i < w:
        count += i

    elif count + i == w:
        count = 0
        finished += 1

    elif count + i > w:
        break

    if finished == h:
        break

if finished == h:
    print("YES")

else:
    print("NO")

