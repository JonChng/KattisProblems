while True:

    a, b = map(int, input().split())

    ans = []
    if a == 0 and b == 0:
        break

    else:
        if a // b == 0:
            whole = 0
            remainder = a % b
            emt = "/"


        else:
            whole = a // b
            remainder = a % b
            emt = "/"


        print(whole, remainder,emt, b)



