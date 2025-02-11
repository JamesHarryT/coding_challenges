def get_vowel_pattern(word):
	vowels = "aeiouAEIOU"
	return ''.join([char.lower() for char in word if char in vowels])

def get_last_word(sentence):
	words = sentence.split()
	lastWord = ""
	for word in reversed(words):
		cleanedWord = "".join([char for char in word if char.isalpha()])
		if cleanedWord:
			lastWord = cleanedWord
			break
	return lastWord.lower()

def doesRhyme(line1, line2):
	lastWord1 = get_last_word(line1)
	lastWord2 = get_last_word(line2)
	output = get_vowel_pattern(lastWord1) == get_vowel_pattern(lastWord2)
	print(output)

# Test cases
doesRhyme("Sam I am!", "Green eggs and ham.")
#output = True
doesRhyme("Sam I am!", "Green eggs and HAM.")
#output = True
# Capitalization and punctuation should not matter.
doesRhyme("You're built like a seat", "I bet you like to eat")
#output = True
doesRhyme("You are off to the races", "a splendid day.")
#output = False
doesRhyme("and frequently do?", "you gotta move.")
#output = False