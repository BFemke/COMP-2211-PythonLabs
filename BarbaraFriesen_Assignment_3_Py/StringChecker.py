#  Name: Barbara Friesen
#  Id: T00721475

def main():
    print("Checking codes...")

    try:
        f_read = open("A3 Codes.txt")
    except IOError:
        print("File Error")
        return

    #creates lists to sort codes
    valid = []
    invalid = []
    restricted = []

    #reads every line in the file
    for line in f_read:
        line = line.rstrip("\n")    #removes trailing \n character

        #if code is valid
        if checkValid(line):
            valid.append(line)  #if code is valid it gets added to valid list

        #if code is invalid
        else:
            invalid.append(line)    #if code is invalid it gets added to invalid list

    f_read.close()

    for code in valid:
        if checkRestricted(code):
            restricted.append(code)

    #print valid codes
    print("\nValid Code(s) are:\n")
    print(valid, "\n")

    #print invalid codes
    print("\nInvalid Code(s) are:\n")
    print(invalid, "\n")

    #print restricted codes
    print("\nInvalid Restricted Code(s) are:\n")
    print(restricted, "\n")

#   Purpose: Checks to see if the given string code is valid or not
#   Input: line - a code string from the file of codes to be checked
#   Output: boolean - true if the code is valid, false otherwise
def checkValid(line):
    
    #if code is at least 10 characters long
    if len(line) >= 10:
        #if position 4 through 7 is a number
        if line[3:7].isdigit():
            #if character at position 10 os a capital letter
            if line[9].isalpha() and line[9].isupper():
                return True #return true because code is valid
            
    return False    #return false because code is invalid

#   Purpose: Checks to see if any of the valid codes do not comply to the new restriction laws
#   Input: code - a valid code string from the array of valid codes
#   Output: boolean - true if the code is restricted, false otherwise
def checkRestricted(code):

    #if access code is restricted
    if code[9] == "R":
        country = int(code[3:7])

        #and if country code is at least 2000
        if country >= 2000:
            return True #code is restricted and returns true
        
    return False    #code not restricted

main()