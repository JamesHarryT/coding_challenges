def convertTime(time):
    actualTime = ''
    isTwelve = False
    isPM = False
    isSingleDigit = False
    hour = 0
    minute = 0
    for i, char in enumerate(time):
        if i == 0:
            hour = int(char) * 10
        if i == 1:
            if char == ':':
                isSingleDigit = True
                hour /= 10
            else:
                hour += int(char)
        if i == 2:
            if isSingleDigit:
                minute = int(char) * 10
            else:
                pass
        if i == 3:
            if isSingleDigit:
                minute += int(char)
            else:
                minute = int(char) * 10
        if i == 4:
            if isSingleDigit == False:
                minute += int(char)
        if char == "p":
            isTwelve = True
            isPM = True
        elif char == "a" or char == "m":
            isTwelve = True
        else:
            pass
    if not isPM and isTwelve and hour == 12: #is 12:00 AM
        hour = 0 
    if isPM:
        hour += 12
    if not isTwelve and hour >= 12:
        hour -= 12
        actualTime = f"{int(hour):02}:{minute:02} pm" 
    elif not isTwelve and hour < 12:
        actualTime = f"{int(hour):02}:{minute:02} am"
    else: 
        actualTime = f"{int(hour):02}:{minute:02}" 
    print(actualTime)
        



convertTime("12:00 am")
#output = "0:00"

convertTime("6:20 pm")
#output = "18:20"

convertTime("21:00")
#output = "9:00 pm"

convertTime("5:05")
#output ="5:05 am"