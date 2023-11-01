string = input()

count = {}

counter = 0


sum = 0

for i in string:
    if i in count:
        count[i] += 1

    else:
        count[i] = 1

possible = True

for i,j in count.items():
    sum += j

for i,j in count.items():

    if sum > 1:
        
        if j % 2 != 0:

            j -= 1
            counter += 1
            sum -= 1

print(counter)









