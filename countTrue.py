
def countTrue(truthArray: list):
    truthCount = 0
    for i in range(len(truthArray)):
        if truthArray[i] == True:
            truthCount += 1
    print(truthCount)


caseOne = [True, False, False, True, False]
caseTwo = [False, False, False, False]
caseThree = []

countTrue(caseOne)
countTrue(caseTwo)
countTrue(caseThree)