e, f, c = map(int, input().split())

empty_bottles = e + f
count = 0

while empty_bottles >= c:

    empty_bottles = empty_bottles - c + 1
    count += 1

print(count)