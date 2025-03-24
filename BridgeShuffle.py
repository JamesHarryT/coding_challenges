def bridgeShuffle(stringOne, stringTwo):
    iterations = 0
    output = []
    if len(stringOne) > len(stringTwo):
        iterations = len(stringOne)
    else:
        iterations = len(stringTwo)
    for i in range(iterations):
        if i < len(stringOne):
            output.append(stringOne[i])
        if i < len(stringTwo):
            output.append(stringTwo[i])
    print(output)

bridgeShuffle(["A", "A", "A"], ["B", "B", "B"])
#output = ["A", "B", "A", "B", "A", "B"]

bridgeShuffle(["C", "C", "C", "C"], ["D"])
#output = ["C", "D", "C", "C", "C"]

bridgeShuffle([1, 3, 5, 7], [2, 4, 6])
#output = [1, 2, 3, 4, 5, 6, 7]