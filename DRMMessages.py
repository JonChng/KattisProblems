import string

alphabets = list(string.ascii_uppercase)

string_1 = input()

mid_point = len(string_1)//2

first_half = string_1[:mid_point]
second_half = string_1[mid_point::]

strings = [first_half, second_half]

all_indexes = []

for i in strings:
    count = 0
    li = list(i)

    for j in li:

        count += alphabets.index(j)

    indexes = []

    for k in li:
        indexes.append(alphabets.index(k))

    rotation = count % 26


    for l in range(len(indexes)):
        indexes[l] += rotation
        if indexes[l] > 25:
            indexes[l] -= 26

    all_indexes.append(indexes)


for i in range(len(all_indexes[0])):

    all_indexes[0][i] += all_indexes[1][i]

    if all_indexes[0][i] > 25:
        all_indexes[0][i] -= 26

ans = "".join(alphabets[pos] for pos in all_indexes[0])
print(ans)












