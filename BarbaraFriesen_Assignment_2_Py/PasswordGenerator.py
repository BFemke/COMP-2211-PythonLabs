def main():
    fname = "1"
    while not fname.isalpha():
        fname = str(input("\nPlease enter first name: ")) #gets first name input from user

        #prints corresponding name input errors
        if fname.isdigit() or (fname.isalnum() and not fname.isalpha()):
            print("Name cannot contain numbers..")
        elif fname == "":
            print("Name cannot be empty..")
        elif fname.isspace():
            print("Name cannot be only whitespace..")

    lname = "1"
    while not lname.isalpha():  
        lname = input("\nPlease enter last name: ") #gets last name input from user

        #prints corresponding name input errors
        if lname.isdigit() or (lname.isalnum() and not fname.isalpha()):
            print("Name cannot contain numbers..")
        elif lname == "":
            print("Name cannot be empty..")
        elif lname.isspace():
            print("Name cannot be only whitespace..")

    id = "1"
    while id.isdigit() or id.isalpha(): 
        id = input("\nPlease enter student ID: ") #gets ID input from user

        #prints corresponding name input errors
        if id.isalpha() or id.isdigit():
            print("ID must be alphanumeric..")
        elif id == "":
            print("ID cannot be empty..")
        elif id.isspace():
            print("ID cannot be only whitespace..")

    #Calls function to generate user name
    user = get_login_name(fname, lname, id)

    valid = False #sets primer to False

    while valid == False:
        password = input("\nPlease enter a password: ") #gets password input from user

        #Calls function to verify password meets requirements
        valid = verify_password(password)

    print("\nGenerated user: ", user) #prints out generated user name
    print("Password: ", password) #prints out accepted password

#function generates login name using first and last names and student id
def get_login_name(fname, lname, id):
    username =""

    fname = fname.capitalize()  #ensures first letter is capitalized

    #add first three characters to username if first name is at least 3 character long
    if len(fname) >= 3:
        username += fname[0:3]

    #Else it adds all characters of first name to username
    else:
        username += fname[0:]

    lname = lname.capitalize()  #ensures first letter is capitalized

    #add first three characters to username if last name is at least 3 character long
    if len(lname) >= 3:
        username += lname[0:3]

    #Else it adds all characters of last name to username
    else:
        username += lname[0:]

    #add last three characters to username if id is at least 3 character long
    if len(id) >= 3:
        username += id[-3:]

    #Else it adds all characters of id name to username
    else:
        username += id[0:]

    return username

#function checks that the password is at least 7 characters long and contains at least
#one uppercase, one lower case, and one digit
def verify_password(password):

    upper = False #Sets primer for checking uppercase letters

    #Loops through each character in password to see if an uppercase letter exists
    for char in password:
        if char.isupper(): #if uppercase letter is found
            upper = True
            break

    lower = False #Sets primer for checking lowercase letters
    #Loops through each character in password to see if an lowercase letter exists
    for char in password:
        if char.islower(): #if lowercase letter is found
            lower = True
            break
    
    #checks if password is at least 7 chharacters long
    if len(password) < 7:
        print("Password must be at least 7 characters long..")
        return False
    
    #Checks if password contains a digit
    elif password.isdigit() or password.isalpha():
        print("Password must be alphanumeric..")
        return False
    
    #Check if password is just empty space
    elif password.isspace():
        print("Password cannot be just empty space..")
        return False
    
    #Checks if password has both upercase and lowercase
    elif(not upper or not lower):
        print("Password must contain at least 1 uppercase and 1 lowercase letter..")
        return False
    
    return True


main()