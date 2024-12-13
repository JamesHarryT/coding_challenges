def isValidPhoneNumber(phoneNumber: str):
    if len(phoneNumber) != 14:
        return False
    
    if (phoneNumber[0] != "(" or phoneNumber[4] != ")" or phoneNumber[5] != " " or phoneNumber[9] != "-"):
        return False
    
    for i in range(len(phoneNumber)):
        if i in [0, 4, 5, 9]:
            continue
        if phoneNumber[i].isdigit() == False:
            return False
        
    return True

print(isValidPhoneNumber("(123) 456-7890"))

print(isValidPhoneNumber("1111)555 2345"))

print(isValidPhoneNumber("098) 123 4567"))