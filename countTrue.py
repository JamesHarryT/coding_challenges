truthArray = [True, False, False, False, False]

def countTrue(truthArray):
    truthCount = 0
    for i in range(len(truthArray)):
        if truthArray[i] == True:
            truthCount += 1
    print(truthCount)


countTrue(truthArray)