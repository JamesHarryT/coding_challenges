def turnCalc(message: int):
    messageAsString = str(message)
    output = ''
    for i in list(messageAsString):
        if i == '1':
            output += 'I'
        elif i == '2':
            output += 'Z'
        elif i == '3':
            output += 'E'
        elif i == '4':
            output += 'H'
        elif i == '5':
            output += 'S'
        elif i == '6':
            output += 'G'
        elif i == '7':
            output += 'L'
        elif i == '8':
            output += 'B'
        elif i == '9':
            output += '-'
        elif i == '0':
            output += 'O'
        else:
            pass
    print(output[::-1])

turnCalc(707)

turnCalc(5508)

turnCalc(3045)

turnCalc('07734') #can't do leading 0