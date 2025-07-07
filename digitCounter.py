def digits(number: int):
    output = 0
    while number > 10:
        number -= 1
        output += len(str(number))
    if number > 0:
        output += number - 1
    print(output)

digits(1)
#output = 0

digits(10)
#output = 9

digits(100)
#output = 189

digits(2020)
#output = 6969