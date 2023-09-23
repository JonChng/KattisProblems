ans = []

for i in range(5):

    string = input()

    for j in range(0, len(string)-2):

        if string[j:j+3] == "FBI":
            ans.append(i+1)

if len(ans) == 0:
    print("HE GOT AWAY!")

else:
    print(" ".join(str(i) for i in ans))


