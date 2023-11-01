

string = input()

dictionary = {}
odd = 0
odd_keys = []
to_remove = 0

for i in string:
    if i in dictionary:
        dictionary[i] += 1

    else:
        dictionary[i] = 1

for key, value in dictionary.items():
    if value % 2 != 0:
        odd += 1
        odd_keys.append(key)

if len(odd_keys) > 1:
    print(len(odd_keys) - 1)

else:
    print(0)








