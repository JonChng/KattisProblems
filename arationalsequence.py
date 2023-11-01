def node_position(p, q):

    moves = []

    while p != q:

        if p > q:
            moves.append("r")
            p -= q

        else:
            moves.append("l")
            q -= p

    nodes = 1
    for i in moves[::-1]:

        nodes *= 2

        if i == "r":
            nodes += 1

    return nodes


n = int(input())

for i in range(n):
    case, fraction = input().split()

    p, q = fraction.split("/")
    case = int(case)
    node = node_position(int(p), int(q))

    print(f"{case} {node}")
