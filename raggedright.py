lines = []
while True:
    line = input()
    if not line:
        break
    lines.append(line)


lengths = []

for i in lines:
    lengths.append(len(i))

longest = max(lengths)

score = 0

for i in lengths[:-1]:
    if i != longest:
        score += (longest - i) ** 2
print(score)






