number_of_cards, prediction, steps = map(int, input().split())

cards = list(range(1, number_of_cards+1))

for i in range(steps):

    choices = input().split(" ")
    numbers = [int(j) for j in choices[1::]]


    if prediction in numbers:
        print("KEEP")

    else:
        print("REMOVE")




