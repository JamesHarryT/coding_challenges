ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", 
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", 
        "sixty", "seventy", "eighty", "ninety"]

def numToEng(num):
    if num >= 100:
        hundreds = ones[num // 100] + " hundred"
        num %= 100
    else:
        hundreds = ""

    if 10 <= num < 20:
        tensAndOnes = teens[num - 10]
    else:
        tens_part = tens[num // 10]
        ones_part = ones[num % 10]
        tensAndOnes = f"{tens_part} {ones_part}".strip()
    if num == 0:
        print("zero")
    else:
        print(f"{hundreds} {tensAndOnes}".strip())

numToEng(0)

numToEng(18)

numToEng(126)

numToEng(909)
