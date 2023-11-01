collation = {}

while True:
    inputs = input()

    if inputs == str(-1):
        break

    else:
        time, question, validity = inputs.split()

        if validity == "wrong":

            if question not in collation.keys():
                collation[question] = {"time":int(time), "count":1, "solved":False}

            else:
                collation[question]["time"] = int(time)
                collation[question]["count"] += 1

        else:

            if validity == "right":
                if question not in collation.keys():
                    collation[question] = {"time":int(time), "count":1, "solved":True}

                else:
                    collation[question]["time"] = int(time) + collation[question]["count"] * 20
                    collation[question]["solved"] = True



solved = 0
sum = 0
for i, j in collation.items():
    if j["solved"]:
        sum += j["time"]
        solved += 1
print(solved, sum)
