def spaceMessage(message):
    output = ""
    index = 0
    while index < len(message):
        char = message[index]
        if char == '[':
            number = ''
            index += 1
            while message[index].isnumeric():
                number += message[index]
                index += 1
            repeatedText = ''
            while message[index] != ']':
                repeatedText += message[index]
                index += 1
            output += repeatedText * int(number)
            index += 1
        else:
            output += char
            index += 1
    print(output)

spaceMessage("ABCD")
spaceMessage("AB[3CD]")
spaceMessage("IF[2E]LG[5O]D")


