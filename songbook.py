minutes, songs = map(int, input().split())

list_of_songs = sorted(list(map(int, input().split())))


max_seconds = minutes * 60

count = 0
number_of_songs = 0

for i in list_of_songs:
    if count + i <= max_seconds:
        count += i
        number_of_songs += 1
print(count)