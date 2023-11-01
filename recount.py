
dictionary = {}

while True:
    s = input()

    if s == "***":
        break

    else:
        if s in dictionary.keys():
            dictionary[s] += 1

        else:
            dictionary[s] = 1

max_val = max(dictionary.values())

count = 0
for i in dictionary.values():
    if i == max_val:
        count += 1

if count > 1:
    print("Runoff!")
else:
    print(max(dictionary, key=dictionary.get))
