def isLongPressed(original, typed):
    i, j = 0, 0
    output = True
    while j < len(typed):
        if i < len(original) and original[i] == typed[j]:
            i += 1
            j += 1
        elif j > 0 and typed[j] == typed[j - 1]:
            j += 1
        else:
            output = False
            break
    if i != len(original):
        output = False
    print(output)




isLongPressed("alex", "aaleex")
#output = true

isLongPressed("saeed", "ssaaedd")
#output = false

isLongPressed("leelee", "lleeelee") 
#output = true

isLongPressed("Tokyo", "TTokkyoh") 
#output = false

isLongPressed("laiden", "laiden") 
#output = true