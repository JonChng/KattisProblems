import string

n = int(input())

letters = list(string.ascii_lowercase)


for i in range(n):
    string = input().lower()
    missing = []
    list_string = list(string)
    for a in letters:
        if a in list_string:
            continue
        else:
            missing.append(a)


    if len(missing) == 0:
        print("pangram")

    else:
        s = "".join(i for i in missing)
        print(f"missing {s}")


