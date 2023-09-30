data_points = int(input())

data = []
for i in range(data_points):
    x, y = map(float, input().split())
    data.append((x, y))

area = 0

for j in range(len(data)-1):
    first_val = (data[j][1] + data[j+1][1])/2
    second_val = data[j+1][0] - data[j][0]

    area += (first_val * second_val)/1000

print(area)
