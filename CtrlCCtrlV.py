def keyboardShortcut(sentence):
    copied = ""
    output = ""
    words = sentence.split()
    for i, word in enumerate(words):
        if word == "Ctrl" and i + 2 < len(words):
            nextWord = words[i + 2]
            if nextWord == "C":
                copied = output
            elif nextWord == "V":
                if copied:
                    output += copied
        elif word not in ["+", "C", "V"]:
            output += word + " "

    print(output)
        



#Example 1
keyboardShortcut("the egg and Ctrl + C Ctrl + V the spoon") 
#output = "the egg and the egg and the spoon"

#Example 2
keyboardShortcut("WARNING Ctrl + V Ctrl + C Ctrl + V")
#output=  "WARNING WARNING"

#Example 3
keyboardShortcut("The Ctrl + C Ctrl + V Town Ctrl + C Ctrl + V")
#output = "The The Town The The Town"