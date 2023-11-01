password1 = input()
password2 = input()

count = 0

for i in range(4):
    if password1[i] != password2[i]:
        count += 1

print(2**count)