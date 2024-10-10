caseOne = "this is pig latin"
caseTwo = "wall street journal"

def pigLatinSentence(normalSentence):
    pigSentence = ''
    movedLetters = ''
    addWay = False
    foundVowel = False
    checkFirstLetter = True
    lastIndex = 0
    for index, letter in enumerate(normalSentence):
        lastIndex = index
    for index, letter in enumerate(normalSentence):
        if checkFirstLetter == True:
            if letter in 'aeiou':
                addWay = True
                checkFirstLetter = False
            else:
                checkFirstLetter = False
                movedLetters += letter
        elif checkFirstLetter == False and addWay == False:
            if letter in 'aeiou':
                foundVowel = True
            if foundVowel == False:
                movedLetters += letter
        if letter == ' ':
            if addWay == True:
                pigSentence += 'way'
            else: 
                pigSentence += (movedLetters + 'ay')
                movedLetters = ''
                foundVowel = False
            pigSentence += ' '
            checkFirstLetter = True
            addWay = False
        elif foundVowel == True or addWay == True:
            pigSentence += letter
        if index == lastIndex:
            if addWay == True:
                pigSentence += 'way'
            else:
                pigSentence += movedLetters + 'ay'
    print(pigSentence)
    

pigLatinSentence(caseOne)
pigLatinSentence(caseTwo)