# diagonal = 2 ** 0.5
#
# code = []
# for i in range(3):
#     code1 = list(map(int, input().split()))
#     code.append(code1)
#
# counter = 1
# sum = 0
#
# while counter < 10:
#
#         for i in range(len(code)):
#
#             for j in range(len(code[i])):
#
#                 if code[i][j] == 1:
#                     if counter == 1:
#                         current_pos_1 = [i, j]
#                         counter += 1
#                     else:
#                         counter = counter
#
#
#
#                 elif code[i][j] == counter:
#                     current_pos_2 = [i, j]
#
#                     if current_pos_1[1] == current_pos_2[1] and (abs(current_pos_2[0] - current_pos_1[0]) == 1 or abs(current_pos_2[0] - current_pos_1[0]) == 2):
#
#                         sum += 1
#                         counter += 1
#                         current_pos_1 = [i, j]
#
#                     elif current_pos_1[0] == current_pos_2[0]:
#
#                         sum += (abs(current_pos_2[1]- current_pos_1[1]))
#                         counter += 1
#
#                         current_pos_1 = [i, j]
#
#
#                     elif abs(current_pos_2[0] - current_pos_1[0]) == 1 and abs(current_pos_2[1] - current_pos_1[1]) == 1:
#
#                         sum += diagonal
#                         counter += 1
#
#                         current_pos_1 = [i, j]
#
#
#                     elif abs(current_pos_2[0] - current_pos_1[0]) == 2 and abs(current_pos_2[1] - current_pos_1[1]) == 2:
#
#                         sum += (diagonal * 2)
#                         counter += 1
#
#                         current_pos_1 = [i, j]
#
#
#
# print(sum)

diagonal = 2 ** 0.5

code = []
for i in range(3):
    code1 = list(map(int, input().split()))
    code.append(code1)

counter = 1
sum = 0

for i in range(len(code)):
    for j in range(len(code[i])):
        if code[i][j] == 1:
            current_pos_1 = [i, j]
            counter += 1
        elif code[i][j] == counter:
            current_pos_2 = [i, j]

            actions = {
                (current_pos_1[1] == current_pos_2[1] and (abs(current_pos_2[0] - current_pos_1[0]) == 1 or abs(current_pos_2[0] - current_pos_1[0]) == 2)): (lambda: sum + 1),
                (current_pos_1[0] == current_pos_2[0]): (lambda: sum + abs(current_pos_2[1]- current_pos_1[1])),
                (abs(current_pos_2[0] - current_pos_1[0]) == 1 and abs(current_pos_2[1] - current_pos_1[1]) == 1): (lambda: sum + diagonal),
                (abs(current_pos_2[0] - current_pos_1[0]) == 2 and abs(current_pos_2[1] - current_pos_1[1]) == 2): (lambda: sum + diagonal * 2),
            }

            for condition, action in actions.items():
                if condition:
                    sum = action()
                    current_pos_1 = [i, j]
                    counter += 1
                    break

print(sum)





