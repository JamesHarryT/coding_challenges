def simon_says(instructions):
    output = 0
    for i in range(len(instructions)):
        number = 0
        command = ""
        isSimon = False
        words = instructions[i].split()
        for word in words:
            if word.isdigit():
                number = int(word)
            if word == "Simon":
                isSimon = True
            if word == "add":
                command = "add"
            if word == "multiply":
                command = "multiply"
            if word == "subtract":
                command = "subtract"
        if isSimon == True:
            match command:
                case "add":
                    output += number
                case "multiply":
                    output *= number
                case "subtract":
                    output -= number
        isSimon = False
        number = 0
        command = ""
    print(output)
                

simon_says([
  "Simon says add 4",
  "Simon says add 6",
  "Then add 5"
])
#output = 10

simon_says([
  "Susan says add 10",
  "Simon says add 3",
  "Simon says multiply by 8"
])
#output = 24

simon_says([
  "Firstly, add 4",
  "Simeon says subtract 100" # Look at the name closely :)
])
#output = 0