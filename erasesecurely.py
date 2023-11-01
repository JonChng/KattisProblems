n = int(input())
before_deletion = list(map(int,input()))
after_deletion = list(map(int, input()))

if n % 2 != 0:
    for i in range(len(before_deletion)):
        if before_deletion[i] == 0:
            before_deletion[i] = 1
        else:
            before_deletion[i] = 0

    if before_deletion == after_deletion:
        print("Deletion succeeded")

    else:
        print("Deletion failed")

else:
    if before_deletion == after_deletion:
        print("Deletion succeeded")

    else:
        print("Deletion failed")
