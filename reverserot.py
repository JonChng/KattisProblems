while True:
    line = input()

    if line == "0":
        break

    else:
        rotation, string = line.split()
        rotation = int(rotation)

        list_of_alphabets = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ_.")

        reversed_string = string[::-1]

        indexes = []

        for i in reversed_string:
            indexes.append(list_of_alphabets.index(i))

        final_letters = []

        for i in indexes:
            new = i + rotation

            if new >= 28:
                new %= 28


            final_letters.append(list_of_alphabets[new])

        print("".join(i for i in final_letters))

