def hoursPassed(start: str, end: str):
    timeOne = int(start.split(":")[0])
    timeTwo = int(end.split(":")[0])
    for i in start.split():
        if i == 'PM':
            timeOne += 12
    for i in end.split():
        if i == 'PM':
            timeTwo += 12
    output = timeTwo - timeOne
    if output == 0:
        print("no time passed")
    else:
        print("%s hours" % output)

hoursPassed("3:00 AM", "9:00 AM")
#output = "6 hours"

hoursPassed("2:00 PM", "4:00 PM")
#output = "2 hours"

hoursPassed("1:00 AM", "3:00 PM")
#output = "14 hours"

hoursPassed("4:00 PM", "4:00 PM")
#output = "no time passed"

