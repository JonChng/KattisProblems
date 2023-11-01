import math

def volume_calculation(x,y):

    height1 = ((4*x + 4*y) + math.sqrt((-4*x - 4*y)**2 - (4*12*x*y)))/24
    height2 = ((4*x + 4*y) - math.sqrt((-4*x - 4*y)**2 - (4*12*x*y)))/24

    vol1 = (x - 2 * height1)*(y - 2 * height1) * height1
    vol2 = (x - 2 * height2)*(y - 2 * height2) * height2

    return max(vol1, vol2)
n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    volume = volume_calculation(x, y)
    print(volume)

