def censor(input: str):
    words = input.split()
    output = ""
    index = 0
    for word in words:
        index += 1
        if len(word) > 4:
            censor = ""
            for i in range(len(word)):
                censor += "*"
            output += censor
        else:
            output += word
        output += " "
    print(output)

censor("The code is fourty")
#output = "The code is ******"

censor("Two plus three is five")
#output = "Two plus ***** is five"

censor("aaaa aaaaa 1234 12345")
#output = "aaaa ***** 1234 *****"
            
