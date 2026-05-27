def sign_up():

    """This function takes no parameters, and prompts the user to enter their userID until they enter a ID that is not in the file. The program then prompts the user to enter a password until a valid password is entered. Then their userID, and a hashed version of their password is saved in the file.

    This function was done by: Gurnit Chopra"""

    previous_userids = []
    filename = "users.csv"
    pword_input = id_input = upper_case = lower_case = digit = symbol = False
    symbols = "!.@#$%^&*()_[]?" # the set of symbols that the user has to incorporate in their password

    print("\n--------Create Account---------\n")

    try:
        with open(filename) as file: # opens the file
            for line in file: # Reads through each line of the file
                temp = line.split(",") # Splits the elements by the comma inbetween them

                if len(line) > 0: # checks if there is something in the line
                    previous_userids.append(temp[0]) # assigns all of the user IDs to the new list

    except FileNotFoundError: # If the file could not be found, it then creates the file

        with open(filename) as file:
            pass
        print("There existed no users.csv file, but one has now been created!")

    while id_input == False: # while the user has entered a invalid userID
        counter = 0
        userid_input = input("Enter your userID: ")

        for p_userid in previous_userids: # runs through each of the previous userID's and checks if what the user enetered is in that list

            if p_userid == userid_input:
                print("This userID is already taken!")
                counter += 1

        if counter >= 1:
            id_input = False

        elif counter == 0:
            id_input = True

    while pword_input == False: # while the user has enetered a invalid password

        print("\n-------------------Password Criteria----------------------------\n")
        print("Enter a password longer than 6 characters")
        print("Enter a password that consists of a upper case character")
        print("Enter a password that consists of a lower case character")
        print("Enter a password that consists of a numerical digit!")
        print("Enter a password that consists of a symbol!\n")

        user_password = input("Enter a password: ")

        for character in user_password: # goes through each character of the password that the user entered and checks if it staisfies it being either uppercase, lowercase, being a digit, or being a symbol from the list above

            if character.isupper() == True:
                upper_case = True

            if character.islower() == True:
                lower_case = True

            if character.isnumeric() == True:
                digit = True

            for symchar in symbols:

                if character == symchar:
                    symbol = True

        if (len(user_password) >= 6 and upper_case == True and lower_case == True and digit == True and symbol == True): # if the users password satifies all the requirements of a valid password
            pword_input = True

        # These set of if statements checks if the password that the user enetered consists of less than 6 characters, no upper case or lower case letter, a digit or a symbol, it then prompts the user their mistake

        if len(user_password) < 6:
            print("Enter a password longer than 6 characters!")

        if upper_case == False:
            print("Enter a password that consists of a upper case character!")

        if lower_case == False:
            print("Enter a password that consists of a lower case character!")

        if digit == False:
            print("Enter a password that consists of a numerical digit!")

        if symbol == False:
            print("Enter a password that consists of a symbol!")

    hash = bcrypt.hashpw(user_password.encode('utf-8'), bcrypt.gensalt() ).decode('utf-8') # hashes the users' valid password

    try:
        with open(filename, "a") as file:

            file.write(userid_input + "," + hash + "\n") # writes to the file, the userID and their hashed password separated by a comma

        print("Authenticating user...")

        sleep(1)

        print("Authenticating user..")

        sleep(1)

        print("\nSuccessfully created account!\n")

    except PermissionError: # Would get caught if the user can't access the file (most likely due to the file being open on the side)
        print("Error, do you have the users.csv file open somewhere else?")
