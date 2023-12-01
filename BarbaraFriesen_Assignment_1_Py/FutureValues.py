
#Function that returns the furture value when provied with the starting
#value, the interest rate, and the number of months
def add_interest(rate, months, startVal):
    #calculates future value using interest formula
    futureVal = startVal * (float(1) + rate) * float(months)
    return futureVal

#Welcomes user
print("Welcome to the interest calculator!")

#Loops until accepted starting balance is given
while True:
    try:
        #Checks if input is numerical
        startVal = float(input("\nPlease enter your starting balance: ")) #grabs input and converts it to float
    except ValueError:
        #Catches exception if input is not numerical
        print("Invalid entry!") #prints error message indicating invalid entry
        continue

    #If the input is between the acceptable ranges the loop is broken
    if 0 < startVal:
        break

    #Prints out of range error message
    print("Your starting balance must be positive..")

#Loops until accepted rate value is given
while True:
    try:
        #Checks if input is numerical
        rate = float(input("\nPlease enter your interest rate: ")) #grabs input and converts it to float
    except ValueError:
        #Catches exception if input is not numerical
        print("Invalid entry!") #prints error message indicating invalid entry
        continue

    #If the input is between the acceptable ranges the loop is broken
    if 0 < rate and rate < 1:
        break

    #Prints out of range error message
    print("The interest value must be greater than 0 and less than 1..")

#Loops until accepted number of months is given
while True:
    try:
        #Checks if input is numerical
        months = int(input("\nPlease enter the number of months to gather interest: ")) #grabs input and converts it to integer
    except ValueError:
        #Catches exception if input is not numerical
        print("Invalid entry!") #prints error message indicating invalid entry
        continue

    #If the input is between the acceptable ranges the loop is broken
    if 1 <= months:
        break

    #Prints out of range error message
    print("The number of months must be at least 1..")

#Calls function to get the future value
futureVal = add_interest(rate, months, startVal)

#Prints our future value
print("\nYour future balance will be ", futureVal)
