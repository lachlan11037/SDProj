from sys import exit  # Import python defined native exit function
from tkinter import * # Import tkinter module for GUI
from tkinter import messagebox #Import tkinter messagebox addon
import re, os  # Import read expression and operating system modules
import random # Import random module to allow generated passwords to be possible

def startMenu(): # Defining the 'startMenu()' function. This function will create a custom made menu that offers to user various choices in order to progress through the program.
    def startUp(): # Defining 'startUp()' function. This function will define what occurs when the user has made a specific selection, with each specific selection calling upon another function.
        startSelect = varStart.get() # Collects user response in GUI and considers the following
        if startSelect == 1: # If the user clicks first circle
            userLogin() # Calls 'userLogin()' function
        if startSelect == 2: # If the user clicks second circle
            userNameCreate() # Calls 'userNameCreate()' function
        if startSelect == 3: # If the user clicks third circle
            messagebox.showinfo("Help", "Lachlans Password Manager/Generator is a password storing program developed in Python. In this program I added functionality to View/Add/Change/Remove Apps and their passwords. In the numbered menus, simply select the circle of the desired function you want to access then hit 'Confirm'.\n\n- Lachlan") # Shows info message for user
        if startSelect == 4: # If the user clicks fourth circle
            exit(0) # Destroy window and end program

    startingWindow = Tk() # Create tk root widget under the name 'passwordChangeWindow' to create the GUI interaction window
    startingWindow.title("STARTUP") # Sets the title of the window to 'STARTUP'
    startingWindow.geometry("1920x1080") # Sets the windows resolution to '1920x1080'
    Label(startingWindow, text="Welcome to Lachlans Password Manager/Generator!", width="300", height="2", font=("Georgia bold", 20)).pack() # Creates a label widget with text in the font 'Georgia bold 20', as well as fit the size of the window to this label with '.pack()'
    Label(startingWindow, text="\nClick the circle of the desired function and press 'Confirm':", width="300", height="2", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    varStart = IntVar(startingWindow) # Creates an int variable under the variable 'varStart' for later use when using radio buttons
    Radiobutton(startingWindow, text='1) Login with existing account', variable=varStart, value=1, height="2", width="30", font=("Arial", 12)).pack() # Creates a radio button that when pressed, will set 'varStart' to value 1
    Radiobutton(startingWindow, text='2) Create new account', variable=varStart, value=2, height="2", width="30", font=("Arial", 12)).pack() # Creates a radio button that when pressed, will set 'varStart' to value 2
    Radiobutton(startingWindow, text='3) Help', variable=varStart, value=3, height="2", width="30", font=("Arial", 12)).pack() # Creates a radio button that when pressed, will set 'varStart' to value 3
    Radiobutton(startingWindow, text='4) Exit', variable=varStart, value=4, height="2", width="30", font=("Arial", 12)).pack() # Creates a radio button that when pressed, will set 'varStart' to value 4
    Button(startingWindow, text="Confirm", command=startUp, height="2", width="30", font=("Arial", 12)).pack() # Creates a button that when pressed, calls the 'startUp' function
    startingWindow.mainloop() # Event loop that allows the GUI interaction window to appear

def mainMenu(): # Defines the 'mainMenu()' function. This function will be the main interface for the user once logged in, allowing for access to all the programs functionalities.
    def menuOption(): # Defines the 'menoOption()'
        menuSelect = varMenu.get() # Collects user response in GUI and considers the following
        if menuSelect == 1:  # If userChoice = 1
            passwordFind()  # Calls 'passwordFind()' function
        if menuSelect == 2:  # If userChoice = 2
            addApp()  # Calls 'addApp()' function
        if menuSelect == 3:  # If userChoice = 3
            passwordChange()  # Calls 'passwordChange()' function
        if menuSelect == 4:  # If userChoice = 4
            if len(userApps) <= 2:  # If the amount of apps in userApps is 2 or less then the user cannot delete any more apps
                messagebox.showerror("Error!", "You must have at least 3 apps before you can remove an app.")  # Display error message
            else:  # Else if the amount of apps is over 2
                removeApp()  # Calls the remove app function
        if menuSelect == 5: # If userChoice = 5
            userDelete() # Calls 'userDelete()' function
        if menuSelect == 6:  # If userChoice = 6
            exportData()  # Calls 'exportData()' function
            exit(0) # Close the window and terminate the program
        else: # Else if a button is not selected and the user hits 'Confirm', do the following
            messagebox.showerror("Error!", "That is not an option!") # Display error message

    menusWindow = Tk() # Create tk root widget under the name 'passwordChangeWindow' to create the GUI interaction window
    menusWindow.title("MENU_WINDOW") # Sets the title of the window to 'MENU_WINDOW'
    menusWindow.geometry("1920x1080") # Sets the resolution of the window to '1920x1080'
    Label(menusWindow, text="Lachlans Password Manager/Generator Menu\nLogged in user: " + userName, width="300", height="6", font=("Georgia bold", 20)).pack() # Creates a label widget with text in the font 'Georgia bold 20', as well as fit the size of the window to this label with '.pack()'
    Label(menusWindow, text="Click the circle of the desired function then hit 'Confirm':\n", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    varMenu = IntVar(menusWindow)
    Radiobutton(menusWindow, text='1) View password for all existing Websites/Apps', variable=varMenu, value=1, height="2", width="50", font=("Arial", 12)).pack() # Creates a radio button that when pressed, will set 'varMenu' to value 1
    Radiobutton(menusWindow, text='2) Add new Website/App and create a password for it', variable=varMenu, value=2, height="2", width="50", font=("Arial", 12)).pack() # Creates a radio button that when pressed, will set 'varMenu' to value 2
    Radiobutton(menusWindow, text='3) Change an existing password for an existing Website/App', variable=varMenu, value=3, height="2", width="50", font=("Arial", 12)).pack() # Creates a radio button that when pressed, will set 'varMenu' to value 3
    Radiobutton(menusWindow, text='4) Remove an existing App/Website', variable=varMenu, value=4, height="2", width="50", font=("Arial", 12)).pack() # Creates a radio button that when pressed, will set 'varMenu' to value 4
    Radiobutton(menusWindow, text='5) Delete Account', variable=varMenu, value=5, height="2", width="50", font=("Arial", 12)).pack() # Creates a radio button that when pressed, will set 'varMenu' to value 5
    Radiobutton(menusWindow, text='6) Exit', variable=varMenu, value=6, height="2", width="50", font=("Arial", 12)).pack() # Creates a radio button that when pressed, will set 'varMenu' to value 6
    Button(menusWindow, text="Confirm", command=menuOption, height="2", width="30", font=("Arial", 12)).pack() # Creates a button that when pressed will call the 'menuOption()' function
    menusWindow.mainloop() # Event loop that allows the GUI interaction window to appear

def userPasswordCreate():  # Defines 'userPincodeCreate()' function. This function will get the entry value from the user in a GUI and use the function below to decide whether or not the entry can be accepted and allow the user to continue with the program.
    def passwordCreate(): # Defines 'pincodeCreate()' function. This function will check the entry value against a bunch of conditions and respond accordingly.
        global userPincode, userEmail, userApps, userPasswords, emailData  # Declares Global Variables
        userPincode = enterPasswordEntry.get()  # Defines 'userPincode' as entry value entered by user in GUI interaction
        if len(userPincode) <= 8:  # If the length of the pincode is 8 or less
            messagebox.showerror("Error!", "Must be at least 8 characters\n")  # Display error message
        if ' ' in userPincode:  # If a space is in user input
            messagebox.showerror("Error!", "Must not contain spaces\n")  # Display error message
        if len(userPincode) >= 20:  # If the user input is greater than 20 characters
            messagebox.showerror("Error!", "Must be shorter than 20 characters\n")  # Display error message
        if not re.search("[a-z]", userPincode):  # If there are non lowercase a-z letters
            messagebox.showerror("Error!", "Must contain at least 1 lowercase\n")  # Display error message
        if not re.search("[0-9]", userPincode):  # If the user input does not contain a number
            messagebox.showerror("Error!", "Must contain at least 1 number\n")  # Display error message
        if not re.search("[A-Z]", userPincode):  # If there are non uppercase A-Z letters then print error and retry
            messagebox.showerror("Error!", "Must contain a least 1 uppercase\n")  # Display error message
        if len(userPincode) >= 8 and len(userPincode) <= 20 and re.search("[A-Za-z0-9]", userPincode) and not ' ' in userPincode:  # If the input contains an uppercase and lowercase letter, has a number and no spaces, and has at least 8 characters and at most 20 characters, then do the following
            emailData = (userEmail.split("@")[1]).split(".")[0].capitalize() # Defines a neatly processed userEmail for later use
            userApps = [str(emailData), 'Code avengers', 'Python turtle']  # Defines 3 Default Apps for the user
            userPasswords = ['undefined', 'undefined','undefined']  # Defines 3 Default Passwords for the apps above for the user
            exportData() # Calls 'exportData()' function
            welcome() # Calls 'mainMenu()' function
        else:  # Else statement incase of some random error that was not picked up by previous error checks
            messagebox.showerror("Error!", "Please make sure your master password follows the rules.")  # Display error message

    enterPasswordWindow = Tk() # Create tk root widget under the name 'enterPasswordWindow' to create the GUI interaction window
    enterPasswordWindow.geometry("1920x1080") # Sets the resolution of the window to '1920x1080'
    enterPasswordWindow.title("ENTER_MASTERPASS") # Sets the title of the window to 'ENTER_MASTERPASS'
    Label(enterPasswordWindow, text="Here you will create your Master Password.", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    Label(enterPasswordWindow, text="\nYour Master Password must:\n\n- Be longer than at least 8 characters\n- Be shorter than at most 20 characters\n- Contain at least 1 lowercase letter\n- Contain at least 1 uppercase letter\n- Contain at least 1 number\n- Contain no spaces", font=("Arial", 14)).pack()  # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    enterPasswordVar = StringVar(enterPasswordWindow) # Creates a string var under the variable 'enterPasswordVar' for later use when using entry field
    enterPasswordEntry = Entry(enterPasswordWindow, textvariable=enterPasswordVar, font=("Arial", 12)) # Creates an entry field for the user to input a response, with that response being in 'Arial 12'
    enterPasswordEntry.pack() # Fit size of the window to this entry field
    Label(enterPasswordWindow, text="Press the button below to successfully create your Master Password", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    Button(enterPasswordWindow, text="Confirm", command=passwordCreate, font=("Arial", 12)).pack() # Creates a button that, when pressed, will call upon the 'passwordCreate' function
    Label(enterPasswordWindow, text="\nOtherwise press the button below to cancel and return to Start Menu:", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    Button(enterPasswordWindow, text="Return", command=startMenu, font=("Arial", 12)).pack() # Creates a button that, when pressed, will call upon the 'startMenu' function
    enterPasswordWindow.mainloop() # Event loop that allows the GUI interaction window to appear

def userDelete():  # Defines 'userDelete()' function. This function will collect a response from the user, and if that response mirrors their master password, the encrypted file of this account will be deleted.
    def deleteUser(): # Defines 'deleteUser()' function. This function will delete the encrypted file if called successfully.
        if userDeleteEntry.get() == userPincode:  # If the user inputs their master password correctly
            os.remove(encrypt(re.sub('[0-9]+', '', userEmail)) + ".txt") # The os module will grab the encrypted file name and remove it from the file
            exit(0) # Exit the program after deleting the file
        else: # Else if the response entered is not the master password of the account
            messagebox.showerror("Error!", "This is not the correct Master Password!") # Display error message

    userDeleteWindow = Tk() # Create tk root widget under the name 'userDeleteWindow' to create the GUI interaction window
    userDeleteWindow.geometry("1920x1080") # Sets the resolution of the window to '1920x1080'
    userDeleteWindow.title("DELETE_ACCOUNT") # Sets the title of the window to 'DELETE_ACCOUNT'
    Label(userDeleteWindow, text="WARNING! THIS ACTION CANNOT BE UNDONE! ", font=("Georgia bold", 20)).pack()  # Creates a label widget with text in the font 'Gerogia bold 20', as well as fit the size of the window to this label with '.pack()'
    Label(userDeleteWindow, text="Enter your Master Password below then hit 'Confirm' to successfully delete this account:", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    userDeleteVar = StringVar(userDeleteWindow) # Creates a string var under the variable 'userDeleteVar' for later use when using entry field
    userDeleteEntry = Entry(userDeleteWindow, textvariable=userDeleteVar, font=("Arial", 12)) # Creates an entry field for the user to input a response, with that response being in 'Arial 12'
    userDeleteEntry.pack() # Fit size of the window to this entry field
    Button(userDeleteWindow, text="Confirm", command=deleteUser, font=("Arial", 12)).pack() # Creates a button that, when pressed, will call upon the 'deleteUser' function
    Label(userDeleteWindow, text="\nOtherwise press the button below to cancel and return to Main Menu:", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    Button(userDeleteWindow, text="Return", command=mainMenu, font=("Arial", 12)).pack() # Creates a button that, when pressed, will call upon the 'mainMenu' function
    userDeleteWindow.mainloop() # Event loop that allows the GUI interaction window to appear

def importData():  # Defines 'importData()' function. This function imports encrypted data from text file into decrypted strings which go into corrosponding variables
    global userApps, userPasswords, userPincode, fileName, userName  # Defines Global Variable names
    userPincode = decrypt(fileName[1])  # Declares pincode for the second line in the users file
    userName = decrypt(fileName[2])  # Declares users name for the third line in the users file
    userApps = []  # Defines app list
    userPasswords = []  # Defines passwords list
    fileName = list(fileName)  # converts fileName as a list
    for app in range(0, len((fileName[3]).split(","))):  # New loop (length of list in the fourth line)
        userApps.append(decrypt((fileName[3]).split(",")[app]))  # Each item in the fourth line is added to the userApps list
    for password in range(0, len((fileName[4]).split(","))):  # New loop (length of list in the fifth line)
        userPasswords.append(decrypt((fileName[4]).split(",")[password]))  # Each item in the fifth line is added to the userPasswords list

def exportData():  # Defines 'exportData()' function. This function exports encrypted strings of user data from the program and puts it neatly into a list
    fileName = open(encrypt(re.sub('[0-9]+', '', userEmail)) + ".txt","w+")  # Sets a encrypted file name (removes numbers due to windows not liking special characters) also creates a new file if one doesnt already exist
    fileName.write("{}\n{}\n{}\n".format(encrypt(userEmail), encrypt(userPincode), encrypt(userName)))  # Writes encrypted strings for user Email, Pincode and Name and stores each item on new line
    for i in range(0, len(userApps)):  # New loop for each item in userApps list
        if i == (len(userApps) - 1):  # If i = the length of a specific userApp
            fileName.write("{}".format(encrypt(userApps[i])))  # |   Places a comma at the end of each item (except the last item)
        else:  # This is for when the strings get imported they are easy for the program to read and seperate
            fileName.write("{}".format(encrypt(userApps[i])) + ",")  # Formats the string correctly
    fileName.write("\n")  # New line to seperate items
    for i in range(0, len(userPasswords)):  # New loop for each item in userPasswords list
        if i == (len(userPasswords) - 1):  # If i = length of a specific userApp
            ending = ""  # Places a comma at the end of each item (except the last item)
        else:  # This is for when the strings get imported they are easy for the program to read and seperate
            ending = ","  # Adds a variable to allow the seperation of strings
        fileName.write("{}".format(encrypt(userPasswords[i])) + ending) # Formats the string correctly
    fileName.close()  # Closes the file (saves)

def passwordFind():  # Defines 'passwordFind()' function. This function will display all current apps and password relationships to the user in a GUI.
    global userApps, userPasswords  # Declares global variabes
    passwordFindWindow = Tk() # Create tk root widget under the name 'passwordChangeWindow' to create the GUI interaction window
    passwordFindWindow.geometry("1920x1080") # Sets the resolution of the window to '1920x1080'
    passwordFindWindow.title("FIND_PASSWORD") # Gives the window the title 'FIND_PASSWORD'
    Label(passwordFindWindow, text="Displaying all current Apps/Websites:".ljust(16), font=("Georgia bold", 20)).pack() # Creates a label widget with text in the font 'Georgia bold 20', as well as fit the size of the window to this label with '.pack()'
    Label(passwordFindWindow, text="".ljust(10) + "App:".ljust(22) + "Password:\n", font=("Arial bold", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    for index in range(0, len(userApps)):  # New loop For the amount of apps in userApps
        Label(passwordFindWindow, text="".ljust(10) + userApps[index].ljust(22) + "\t" + userPasswords[index], font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    Label(passwordFindWindow, text="\nPress the button below to return to the Main Menu.", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    Button(passwordFindWindow, text="Return", command=mainMenu, font=("Arial", 12)).pack() # Creates a button that, when pressed, calls the 'mainMenu' function
    passwordFindWindow.mainloop() # Event loop that allows the GUI interaction window to appear

def passwordChange():   # Defines 'passwordChange()' function. This function will ask the user to input a number corresponding with the app/password relationship the user wishes to change.
                        # The user will then enter the password they want the app to be partnered with. If both entries pass the requirements set in the 'changePassword()' function the password will be changed.
                        # This is all done through a GUI interaction created within this function.
    def changePassword(): # Defines 'changePassword()' function. This function sets the requirements that the user's entries must pass in order to successfully complete the given task.
        global userPasswords  # Declare global variables to allow efficient coding
        try: # Create a try statement for everything below until 'except ValueError:'
            userChoice = int(passwordChangeNumEntry.get()) # Assign the user's input for app/password list number to the variable 'userChoice'
            if userChoice in range(1, len(userApps) + 1):  # If the user's inputted number is in the menu, do the following
                newChoice = passwordChangeAppEntry.get() # Assign user's input for new password to the variable 'newChoice'
                if len(newChoice) >= 8 and len(newChoice) <= 20:  # If the length of the inputted password is greater than or equal to 4, do the following
                    userPasswords[userChoice - 1] = newChoice # Successfully assign new password to the desired app
                    exportData()  # Export this data for later viewing by calling 'exportData()' function
                    mainMenu()  # Return to the main menu by calling 'mainMenu()' function
                else:  # If the length of the inputted password is less than 4, do the following
                    messagebox.showerror("Error!", "It is recommended that you new password is longer than or equal to 8 characters and shorter than or equal to 20 characters!")  # Display messagebox showing error message
            else:  # If the user inputted a number that is not in the menu, do the following
                messagebox.showerror("Error!", "Please only enter numbers on the menu!")  # Display messagebox showing error message
        except ValueError:  # If the user input is a string rather than an int or if a box is left unfilled, do the following
            messagebox.showerror("Error!", "Please make sure you fill out all the boxes correctly!")  # Display messagebox showing error message

    passwordChangeWindow = Tk() # Create tk root widget under the name 'passwordChangeWindow' to create the GUI interaction window
    passwordChangeWindow.geometry("1920x1080") # Sets the resolution of the window to '1920x1080'
    passwordChangeWindow.title("CHANGE_PASSWORD") # Gives the window the title 'CHANGE_PASSWORD'
    Label(passwordChangeWindow, text="".ljust(10) + "App:".ljust(22) + "Password:\n", font=("Arial", 14)).pack()  # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    for i in range(0, len(userApps)):  # Starts new loop for the amount of items in userApps list and gives them all corresponding numbers
        Label(passwordChangeWindow, text="".ljust(5) + "{}".format(i + 1) + ") " + userApps[i].ljust(20) + "\t" + userPasswords[i], font=("Arial", 14)).pack()  # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    Label(passwordChangeWindow, text="\nPlease enter the number for the password you want to change: ", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    passwordChangeNumVar = StringVar(passwordChangeWindow) # Creates a string variable under the variable 'passwordChangeNumVar' for later use when creating Entry field
    passwordChangeNumEntry = Entry(passwordChangeWindow, textvariable=passwordChangeNumVar, font=("Arial", 12)) # Creates an Entry field for the user to input app/password list number in the font 'Arial 12'
    passwordChangeNumEntry.pack() # Fit the size of the window to this Entry field with '.pack()'
    Label(passwordChangeWindow, text="Enter the new password for the selected app: ", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    passwordChangeAppVar = StringVar(passwordChangeWindow) # Creates a string variable under the variable 'passwordChangeAppVar' for later use when creating Entry field
    passwordChangeAppEntry = Entry(passwordChangeWindow, textvariable=passwordChangeAppVar, font=("Arial", 12)) # Creates an Entry field for the user to input new password in the font 'Arial 12'
    passwordChangeAppEntry.pack() # Fit the size of the window to this Entry field with '.pack()'
    Label(passwordChangeWindow, text="Press the button below to successfully register your new password for the chosen app and return to the Main Menu.", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    Button(passwordChangeWindow, text="Confirm", command=changePassword, font=("Arial", 12)).pack() # Creates a button that, when pressed, calls 'changePassword()' function. The text of this button is in the font 'Arial 12'
    Label(passwordChangeWindow, text="\nIf you do not want to change an apps password, press the button below to return to the Main Menu without any adjustments being made.", font=("Arial", 14)).pack()  # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    Button(passwordChangeWindow, text="Return", command=mainMenu, font=("Arial", 12)).pack()  # Creates a button that, when pressed, calls 'mainMenu()' function. The text of this button is in the font 'Arial 12'
    Label(passwordChangeWindow, text="\n Alternatively, you may change an existing password to a randomised program created password. To do this press the button below.", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    Button(passwordChangeWindow, text="Generate", command=passwordGenerationChange, font=("Arial", 12)).pack() # Creates a button that, when pressed, calls the 'passwordGenerationChange' function
    passwordChangeWindow.mainloop() # Event loop that allows the GUI interaction window to appear

def passwordGenerationChange(): # Defines 'passwordGenerationChange()' function. This function will ask the user to input the numbered app they would like to change the password for, with that password being randomly generated based on user response on length.
    def generatePassword(): # Defines 'generatePassword()' function. This function will set the rules that the response of the user must meet, as well as generate a password and change the original.
        global userPasswords  # Declare global variables to allow efficient coding
        try:  # Create a try statement for everything below until 'except ValueError:'
            userNum = int(generatePasswordNumEntry.get())  # Assign the user's input for app/password list number to the variable 'userNum'
            if userNum in range(1, len(userApps) + 1):  # If the user's inputted number is in the menu, do the following
                genPass = int(generatePasswordAppEntry.get())  # Assign user's input for new password to the variable 'genPass'
                if genPass >= 8 and genPass <= 20:  # If the length of the inputted password is greater than or equal to 4, do the following
                        possibleCharacters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ" # Assign the 'possibleCharacters' variable to any lowercase letter, uppercase letter, and single digit numbers
                        passwordGenerated = "".join(random.sample(possibleCharacters, genPass)) # Assign the 'passwordGenerated' variable to a randomly generated password with response length in mind
                        userPasswords[userNum - 1] = passwordGenerated  # Successfully assign new password to the desired app
                        exportData()  # Export this data for later viewing by calling 'exportData()' function
                        mainMenu()  # Return to the main menu by calling 'mainMenu()' function
                else:  # If the length of the inputted password is less than 4, do the following
                    messagebox.showerror("Error!", "It is recommended that you make your generated password longer than or equal to 8 characters and shorter than or equal to 20 characters!")  # Display messagebox showing error message
            else:  # If the user inputted a number that is not in the menu, do the following
                messagebox.showerror("Error!", "Please only enter numbers on the menu!")  # Display messagebox showing error message
        except ValueError:  # If the user input is a string rather than an int or if a box is left unfilled, do the following
            messagebox.showerror("Error!", "Please make sure you fill out all the boxes correctly!")  # Display messagebox showing error message

    generatePasswordWindow = Tk()  # Create tk root widget under the name 'passwordChangeWindow' to create the GUI interaction window
    generatePasswordWindow.geometry("1920x1080")  # Sets the resolution of the window to '1920x1080'
    generatePasswordWindow.title("GENERATE_PASSWORD")  # Gives the window the title 'CHANGE_PASSWORD'
    Label(generatePasswordWindow, text="".ljust(10) + "App:".ljust(22) + "Password:\n", font=("Arial", 14)).pack()  # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    for i in range(0, len(userApps)):  # Starts new loop for the amount of items in userApps list and gives them all corresponding numbers
        Label(generatePasswordWindow, text="".ljust(5) + "{}".format(i + 1) + ") " + userApps[i].ljust(20) + "\t" + userPasswords[i], font=("Arial", 14)).pack()  # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    Label(generatePasswordWindow, text="\nPlease enter the number for the password you want to change: ", font=("Arial", 14)).pack()  # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    generatePasswordNumVar = StringVar(generatePasswordWindow)  # Creates a string variable under the variable 'passwordChangeNumVar' for later use when creating Entry field
    generatePasswordNumEntry = Entry(generatePasswordWindow, textvariable=generatePasswordNumVar, font=("Arial", 12))  # Creates an Entry field for the user to input app/password list number in the font 'Arial 12'
    generatePasswordNumEntry.pack()  # Fit the size of the window to this Entry field with '.pack()'
    Label(generatePasswordWindow, text="How many characters long would you like your generated password for this app to be?", font=("Arial", 14)).pack()  # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    generatePasswordAppVar = StringVar(generatePasswordWindow)  # Creates a string variable under the variable 'passwordChangeNumVar' for later use when creating Entry field
    generatePasswordAppEntry = Entry(generatePasswordWindow, textvariable=generatePasswordAppVar, font=("Arial", 12))  # Creates an Entry field for the user to input app/password list number in the font 'Arial 12'
    generatePasswordAppEntry.pack()  # Fit the size of the window to this Entry field with '.pack()'
    Label(generatePasswordWindow, text="\nPress the button below to successfully register your randomly generated password for the chosen app and return to the Main Menu", font=("Arial", 14)).pack()
    Button(generatePasswordWindow, text="Confirm", command=generatePassword, font=("Arial", 12)).pack()
    Label(generatePasswordWindow, text="\nIf you do not want to change your password, press the button below to return to the Main Menu without any adjustments being made.", font=("Arial", 14)).pack()  # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    Button(generatePasswordWindow, text="Return", command=mainMenu, font=("Arial", 12)).pack()  # Creates a button that, when pressed, calls 'mainMenu()' function. The text of this button is in the font 'Arial 12'
    generatePasswordWindow.mainloop()  # Event loop that allows the GUI interaction window to appear

def removeApp():    # Defines 'removeApp()' function. This function will ask the user to input a number with the corresponding app/password relationship the user wishes to remove, only after passing the requirements.
                    # This is all done through a GUI interaction created within this function.
    def appRemove():    # Defines 'appRemove()' function. This function sets the requirements that the user's entries must pass in order to successfully complete the given task.
        global userPasswords, userApps  # Declares global Variables
        try:  # Create a try statement for everything below until 'except ValueError:'
            userChoice = int(removeAppEntry.get())  # Assign the user's input to the variable 'userChoice'
            if userChoice in range(1, len(userApps) + 1):  # If the user inputted a number that was on the list, do the following
                del userApps[userChoice - 1]  # Deletes that particular app
                del userPasswords[userChoice - 1]  # Deletes that particular password
                mainMenu()  # Calls 'mainMenu()' function, returning to the Main Menu
            else:  # If the user entered a number that wasn't on the list, do the following
                messagebox.showerror("Error!", "Please only enter numbers on the menu")  # Display messagebox showing error message
        except ValueError:  # If the input was a string rather than an int or a box was left unfilled, do the following
            messagebox.showerror("Error!", "Please make sure you fill out all the boxes correctly!")  # Display messagebox showing error message

    removeAppWindow = Tk()  # Create tk root widget under the name 'removeAppWindow' to create the GUI interaction window
    removeAppWindow.geometry("1920x1080")  # Sets the resolution of the window to '1920x1080'
    removeAppWindow.title("REMOVE_APP")   # Gives the window the title 'REMOVE_APP'
    Label(removeAppWindow, text="".ljust(10) + "App:".ljust(22) + "Password:\n", font=("Arial", 14)).pack()  # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    for i in range(0, len(userApps)):  # Starts new loop for the amount of items in userApps list and gives them all corresponding numbers
        Label(removeAppWindow, text="".ljust(5) + "{}".format(i + 1) + ") " + userApps[i].ljust(20) + "\t" + userPasswords[i], font=("Arial", 14)).pack()  # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    Label(removeAppWindow, text="\nPlease enter the number for the app you want to remove: ", font=("Arial", 14)).pack()  # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    removeAppVar = StringVar(removeAppWindow)  # Creates a string variable under the variable 'removeAppVar' for later use when creating Entry field
    removeAppEntry = Entry(removeAppWindow, textvariable=removeAppVar, font=("Arial", 12))  # Creates an Entry field for the user to input app/password list number
    removeAppEntry.pack()  # Fit the size of the window to this Entry field with '.pack()'
    Label(removeAppWindow, text="Press the button below to successfully remove the chosen app and return to the Main Menu.", font=("Arial", 14)).pack()  # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    Button(removeAppWindow, text="Confirm", command=appRemove, font=("Arial", 12)).pack()  # Creates a button that, when pressed, calls 'appRemove()' function. The text inside this button is in the font 'Arial 12'.
    Label(removeAppWindow, text="\nIf you do not want to remove an app, press the button below to return to the Main Menu without any adjustments being made.", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    Button(removeAppWindow, text="Return", command=mainMenu, font=("Arial", 12)).pack() # Creates a button that, when pressed, calls 'mainMenu()' function. The text inside this is in the font 'Arial 12'.
    removeAppWindow.mainloop()  # Event loop that allows the GUI interaction window to appear

def addApp():   # Define 'addApp()' function. This function will ask the user to input an app and a password respectivelly, and if it passes the requirements gets added to the list of existing apps/passwords
                # This is all done through a GUI interaction created within this function.
    def appAdd():  # Defines 'appAdd()' function. This function sets the requirements that the user's entries must pass in order to successfully complete the given task.
        global userApps, userPasswords  # Calls global variables
        if len(addAppWebEntry.get()) > 1 and len(addAppWebEntry.get()) <= 30:  # If the app name the user entered is greater than the length of 1 or smaller than or equal to 30, do the following
            if len(addAppPassEntry.get()) >= 8 and len(addAppPassEntry.get()) <= 20:  # If the password length the user entered is greater than 4 characters, do the following
                userPasswords.append(addAppPassEntry.get())  # Add the password to the password list
                userApps.append(addAppWebEntry.get())  # Add the app to the app list
                exportData()  # Exports user data to file
                mainMenu()  # Calls 'mainMenu()' function, returning to the Main Menu
            else:  # If the user entered a password that has a length smaller than or equal to 4, do the following
                messagebox.showerror("Error!", "It is recommended that your password is more than or equal to 8 characters and less than or equal to 20 characters!")  # Display messagebox showing error message
        else: # If the user entered an app that has a length smaller than or equal to 1, do the following
            messagebox.showerror("Error!", "Your app has to be longer than 1 character and shorter than or equal to 30 characters!") # Display messagebox showing error message

    addAppWindow = Tk() # Create tk root widget under the name 'addAppWindow' to create the GUI interaction window
    addAppWindow.geometry("1920x1080") # Sets the resolution of the window to '1920x1080'
    addAppWindow.title("ADD_APP") # Gives the window the title 'ADD_APP'
    Label(addAppWindow, text="Please enter the name of the Website/App:", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    addAppWebVar = StringVar(addAppWindow) # Creates a string variable under the variable 'addAppWebVar' for later use when creating Entry field
    addAppWebEntry = Entry(addAppWindow, textvariable=addAppWebVar, font=("Arial", 12)) # Creates an Entry field for the user to input the app
    addAppWebEntry.pack() # Fit the size of the window to this Entry field with '.pack()'
    Label(addAppWindow, text="Please enter the password for this Website/App:", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    addAppPassVar = StringVar(addAppWindow) # Creates a string variable under the variable 'addAppPassVar' for later use when creating Entry field
    addAppPassEntry = Entry(addAppWindow, textvariable=addAppPassVar, font=("Arial", 12)) # Creates an Entry field for the user to input the password
    addAppPassEntry.pack() # Fit the size of the window to this Entry field with '.pack()'
    Label(addAppWindow, text="Press the button below to successfully register these details and return to the Main Menu.", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    Button(addAppWindow, text="Confirm", command=appAdd, font=("Arial", 12)).pack() # Creates a button that, when pressed, calls 'appAdd()' function. The text inside this is in the font 'Arial 12'.
    Label(addAppWindow, text="\nIf you do not want to add an app, press the button below to return to the Main Menu without any adjustments being made.", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    Button(addAppWindow, text="Return", command=mainMenu, font=("Arial", 12)).pack() # Creates a button that, when pressed, calls 'mainMenu()' function. The text inside this is in the font 'Arial 12'.
    Label(addAppWindow, text="\n Alternatively, you may let the program create randomised password. To do this press the button below.", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    Button(addAppWindow, text="Generate", command=passwordGenerationAdd, font=("Arial", 12)).pack() # Creates a button that, when pressed, calls 'passwordGenerationAdd()' function. The text inside this is in the font 'Arial 12'.
    addAppWindow.mainloop() # Event loop that allows the GUI interaction window to appear

def passwordGenerationAdd(): # Defines 'passwordGenerationAdd()' function. This function will collect the response the user inputted for the new name of their app, and the number of characters they would like to have generated for their password. This information is then passed to 'generatePassword()' function.
    def generatePassword(): # Defines 'generatePassword()' function. This function will use information collected to evaluate if the responses follow the set out rules or not, then acts accordingly
        global userPasswords, userApps  # Declare global variables to allow efficient coding
        if len(generatePasswordAppEntry.get()) > 1 and len(generatePasswordAppEntry.get()) <= 30:  # If the app name the user entered is greater than the length of 1 and shorter than or equal to the length of 30, do the following
            try: # Do the following unless ValueError encountered
                genPass = int(generatePasswordPassEntry.get())  # Assign user's input for new password to the variable 'genPass'
                if genPass >= 8 and genPass <= 20:  # If the length of the inputted password is greater than or equal to 4, and smaller or equal to 20, do the following
                        possibleCharacters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ" # Set variable 'possibleCharacters' to every number 1 digit number, lowercase letter and uppercase letter
                        passwordGenerated = "".join(random.sample(possibleCharacters, genPass)) # Set variable 'passwordGenerated' to the newly created password
                        userPasswords.append(passwordGenerated)  # Add the password to the password list
                        userApps.append(generatePasswordAppEntry.get())  # Add the app to the app list
                        exportData()  # Exports user data to file
                        mainMenu()  # Calls 'mainMenu()' function, returning to the Main Menu
                else:  # If the length of the inputted password is less than 4, do the following
                    messagebox.showerror("Error!", "It is recommended that you make your generated password longer than or equal to 8 characters and shorter than or equal to 20 characters!")  # Display messagebox showing error message
            except ValueError: # If the character box is left empty or contains string, do the following
                messagebox.showerror("Error!", "Please make sure you fill out all the boxes correctly!")  # Display messagebox showing error message
        else:  # If the user inputted an app that is smaller than or equal to character length 1, do the following
            messagebox.showerror("Error!", "Please ensure that your app is longer than 1 character and shorter than or equal to 30 characters!")  # Display messagebox showing error message

    generatePasswordWindow = Tk()  # Create tk root widget under the name 'generatePasswordWindow' to create the GUI interaction window
    generatePasswordWindow.geometry("1920x1080")  # Sets the resolution of the window to '1920x1080'
    generatePasswordWindow.title("GENERATE_PASSWORD")  # Gives the window the title 'GENERATE_PASSWORD'
    Label(generatePasswordWindow, text="\nPlease enter the name of the Website/App: ", font=("Arial", 14)).pack()  # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    generatePasswordAppVar = StringVar(generatePasswordWindow)  # Creates a string variable under the variable 'passwordChangeNumVar' for later use when creating Entry field
    generatePasswordAppEntry = Entry(generatePasswordWindow, textvariable=generatePasswordAppVar, font=("Arial", 12))  # Creates an Entry field for the user to input app/password list number in the font 'Arial 12'
    generatePasswordAppEntry.pack()  # Fit the size of the window to this Entry field with '.pack()'
    Label(generatePasswordWindow, text="How many characters long would you like your generated password for this app to be?", font=("Arial", 14)).pack()  # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    generatePasswordPassVar = StringVar(generatePasswordWindow)  # Creates a string variable under the variable 'passwordChangeNumVar' for later use when creating Entry field
    generatePasswordPassEntry = Entry(generatePasswordWindow, textvariable=generatePasswordPassVar, font=("Arial", 12))  # Creates an Entry field for the user to input app/password list number in the font 'Arial 12'
    generatePasswordPassEntry.pack()  # Fit the size of the window to this Entry field with '.pack()'
    Label(generatePasswordWindow, text="\nPress the button below to successfully register your randomly generated password for the chosen app and return to the Main Menu", font=("Arial", 14)).pack()
    Button(generatePasswordWindow, text="Confirm", command=generatePassword, font=("Arial", 12)).pack() # Creates a button that, when pressed, calls 'generatePassword' function.
    Label(generatePasswordWindow, text="\nIf you do not want to change your password, press the button below to return to the Main Menu without any adjustments being made.", font=("Arial", 14)).pack()  # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    Button(generatePasswordWindow, text="Return", command=mainMenu, font=("Arial", 12)).pack()  # Creates a button that, when pressed, calls 'mainMenu()' function. The text of this button is in the font 'Arial 12'
    generatePasswordWindow.mainloop()  # Event loop that allows the GUI interaction window to appear

def userLogin():  # Defines 'userLogin()' function. This function will create a GUI for the user to input their already registered email to continue the login phase, checks if response meets rules set out in 'enterEmail()' function.
    def enterEmail(): # Defines 'enterEmail()' function. This function will check the response of the user and act accordingly
        global fileName, userEmail  # Declares global variables
        try:  # Try unless exception
            fileName = open(encrypt(re.sub('[0-9]+', '', userLoginEmailEntry.get())) + ".txt", "r").read().split()  # attemps to open the email (Remove numbers due to encryption)
            if decrypt(fileName[0]) == userLoginEmailEntry.get():  # Verifies the input by checking it against the email in the file
                userEmail = userLoginEmailEntry.get() # Define userEmail as the entry value entered by user
                passLogin() # Calls 'passLogin()' function
            else: # Should except function not work for whatever reason do this
                messagebox.showerror("Error!", "This email doesn't exist in the database!")  # Display messagebox showing this message
        except FileNotFoundError:  # If the file does not exist then do the following
                messagebox.showerror("Error!", "This email doesn't exist in the database!")  # Display messagebox showing this messag
    userLoginEmailWindow = Tk() # Create tk root widget under the name 'userLoginEmailWindow' to create the GUI interaction window
    userLoginEmailWindow.geometry("1920x1080") # Sets the resolution of the window to '1920x1080'
    userLoginEmailWindow.title("USER_LOGIN") # Gives the window the title 'USER_LOGIN'
    Label(userLoginEmailWindow, text="Please enter your registered Email address: ", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    userLoginEmailVar = StringVar(userLoginEmailWindow) # Creates a string variable under the variable 'userLoginEmailVar' for later use when creating Entry field
    userLoginEmailEntry = Entry(userLoginEmailWindow, textvariable=userLoginEmailVar, font=("Arial", 12)) # Creates an Entry field for the user to input app/password list number in the font 'Arial 12'
    userLoginEmailEntry.pack() # Fit the size of the window to this Entry field with '.pack()'
    Label(userLoginEmailWindow, text="Press the button below to successfully confirm your Email address:", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    Button(userLoginEmailWindow, text="Confirm", command=enterEmail, font=("Arial", 12)).pack() # Creates a button that, when pressed, calls the 'enterEmail' function
    Label(userLoginEmailWindow, text="\nOtherwise press the button below to cancel and return to Start Menu:", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    Button(userLoginEmailWindow, text="Return", command=startMenu, font=("Arial", 12)).pack() # Creates a button that, when pressed, calls the 'startMenu' function
    userLoginEmailWindow.mainloop() # Event loop that allows the GUI interaction window to appear

def passLogin(): # Defines 'pinLogin()' function. This function will get a response from the user, and if this response is the same as the master password accociated with their previously registered email, then continue the program.
    def enterPass(): # Define 'enterPin()' function. This function will check if the response is valid or not and act accordingly
        global userPincode # Defines lobal variables
        if decrypt(fileName[1]) == userLoginPinEntry.get():  # If the pincode entered matches the pincode in the file
            userPincode = userLoginPinEntry.get() # Defines userPincode as the entry value entered by user
            importData()  # Import the text file
            mainMenu()  # Calls 'mainMenu' function
        else:  # If pincode doesnt match pincode in file
            messagebox.showerror("Error!", "Incorrent Master Password!")  # Display messagebox showing this message

    userLoginPinWindow = Tk() # Create tk root widget under the name 'userLoginPinWindow' to create the GUI interaction window
    userLoginPinWindow.geometry("1920x1080") # Sets the resolution of the window to '1920x1080'
    userLoginPinWindow.title("PASS_LOGIN") # Gives the window the title 'PASS_LOGIN'
    Label(userLoginPinWindow, text="Email Entered: " + userEmail, font=("Arial bold", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    Label(userLoginPinWindow, text="Please enter the Master Password linked with this Email: ", font=("Arial ", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    userLoginPinVar = StringVar(userLoginPinWindow) # Assign the 'userLoginPinVar' var to a string var
    userLoginPinEntry = Entry(userLoginPinWindow, textvariable=userLoginPinVar, show="*", font=("Arial", 12)) # Creates an entry box for the user to input a response, with that response being in 'Arial 12'
    userLoginPinEntry.pack() # Fits the size of the window to the entry box
    Label(userLoginPinWindow, text="Press the button below to successfully confirm your Master Password:", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    Button(userLoginPinWindow, text="Confirm", command=enterPass, font=("Arial", 12)).pack() # Creates a button that, when pressed, calls the 'enterPass' function
    Label(userLoginPinWindow, text="\nOtherwise press the button below to cancel and return to Start Menu:", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    Button(userLoginPinWindow, text="Return", command=startMenu, font=("Arial", 12)).pack() # Creates a button that, when pressed, calls the 'startMenu' function
    userLoginPinWindow.mainloop() # Event loop that allows the GUI interaction window to appear

def userEmailCreate(): # Defines 'userEmailCreate()' function. This function will get a response from the user and use that response as the email for the new account if it passes the rules.
    def emailCreate(): # Define 'emailCreate()' function. This functions will check if the response follows the rules and reacts accordingly
        global userEmail  # Declares global variables
        if len(enterEmailEntry.get()) > 50: # If the character length of the response is over 50, do the following
            messagebox.showerror("Error!", "Your email must be shorter than or equal to 50 characters!") # Display messagebox showerror
        else: # Else if the length of the response is equal to or under 50, do the following
            if re.match(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)",enterEmailEntry.get()):  # Check email for no special characters
                if os.path.isfile(encrypt(re.sub('[0-9]+', '',enterEmailEntry.get())) + ".txt"):  # Check if the user already exists so there will be no duplicates
                    messagebox.showerror("Error!", "This email already exists within the database! Try again!")  # Alerts the user that this user already exists, the user must input a different email
                else:  # If the user does not already exist
                    userEmail = enterEmailEntry.get() # Define userEmail as entry value entered by user
                    userPasswordCreate() # Call 'userPasswordCreate()' function
            else:  # Else if input does not contain '@', a '.', or special characters are inserted
                messagebox.showerror("Error!", "Invalid formatting! Emails must contain an '@', followed by a character(s), followed by a '.', followed by a character(s). \nEg: BigNose14@gmail.com")  # Display messagebox showing this message

    enterEmailWindow = Tk() # Create tk root widget under the name 'enterEmailWindow' to create the GUI interaction window
    enterEmailWindow.geometry("1920x1080") # Sets the resolution of the window to '1920x1080'
    enterEmailWindow.title("ENTER_EMAIL") # Gives the window the title 'ENTER_EMAIL'
    Label(enterEmailWindow, text="Please enter your Email address: ", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    enterEmailVar = StringVar(enterEmailWindow) # Assign the 'enterEmailVar' var to a string var
    enterEmailEntry = Entry(enterEmailWindow, textvariable=enterEmailVar, font=("Arial", 12)) # Creates an entry box for the user to input a response, with that response being in 'Arial 12'
    enterEmailEntry.pack() # Fits the size of the window to the entry box
    Label(enterEmailWindow, text="Press the button below to successfully create your login Email address", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    Button(enterEmailWindow, text="Confirm", command=emailCreate, font=("Arial", 12)).pack() # Creates a button that, when pressed, calls the 'emailCreate' function
    Label(enterEmailWindow, text="\nOtherwise press the button below to cancel and return to Start Menu:", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    Button(enterEmailWindow, text="Return", command=startMenu, font=("Arial", 12)).pack() # Creates a button that, when pressed, calls the 'startMenu' function
    enterEmailWindow.mainloop() # Event loop that allows the GUI interaction window to appear

def userNameCreate(): # Define 'userNameChange()' function. This function will get a response from the user and use that response as the username for the new account if it passes the rules.
    def userCreate(): # Define 'userCreate()' function. This function will check if hte response follows the rules and reacts accordingly.
        global userName # Declares global variables
        userName = enterNameEntry.get() # Define userName as entry value entered
        if len(userName) > 15:  # If the name is more than 15 Characters then alert user
            messagebox.showerror("Error!", "Maximum 15 characters allowed!") # Display messagebox showing this message
        if len(userName) < 2:  # If the name is more than 15 Characters then alert user
            messagebox.showerror("Error!", "Must have at least 2 characters!")  # Display messagebox showing this message
        if not re.match("^[a-z,A-Z]*$", userName):  # Allows for capitals and lower case but not numbers or any other symbols
            messagebox.showerror("Error!", "Only the letters a-z are allowed!")  # Display messagebox showing this message
        if len(userName) <= 15 and len(userName) >= 2 and re.match("^[a-z,A-Z]*$",userName):  # If the name input is less than 15 characters, is greater than or equal to 2 characters, and contains no numbers or special characters
            userEmailCreate() # Calls 'userEmailCreate()' function

    enterNameWindow = Tk() # Create tk root widget under the name 'enterNameWindow' to create the GUI interaction window
    enterNameWindow.geometry("1920x1080") # Sets the resolution of the window to '1920x1080'
    enterNameWindow.title("ENTER_FIRST_NAME") # Gives the window the title 'ENTER_FIRST_NAME'
    enterNameVar = StringVar(enterNameWindow) # Assign the 'enterNameVar' var to a string var
    Label(enterNameWindow, text="Please enter your first name: ", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    enterNameEntry = Entry(enterNameWindow, textvariable=enterNameVar, font=("Arial", 12)) # Creates an entry box for the user to input a response, with that response being in 'Arial 12'
    enterNameEntry.pack() # Fits the size of the window to the entry box
    Label(enterNameWindow, text="Press the button below to successfully create your display name:", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    Button(enterNameWindow, text="Confirm", command=userCreate, font=("Arial", 12)).pack() # Creates a button that, when pressed, calls the 'userCreate' function
    Label(enterNameWindow, text="\nOtherwise press the button below to cancel and return to Start Menu:", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    Button(enterNameWindow, text="Return", command=startMenu, font=("Arial", 12)).pack() # Creates a button that, when pressed, calls the 'startMenu' function
    enterNameWindow.mainloop() # Event loop that allows the GUI interaction window to appear

def encrypt(txt):  # Rotation Encryption function (5 forward alphabetical rotations) (THIS IS ONE OF THE COMPLEX ALGORITHMS)
    encrypted = ''  # Clears string cache
    for i in txt:  # New loop (len of txt)
        c = ord(i) + 5  # Ord gets the ASCII value for a character and increases its value by 5
        if ord(i) != c:  # If c is a n
            b = chr(c)  # b equals the character of the ASCII value
            encrypted += b  # Adds each character to the encrypted string
    encrypted = str(encrypted.replace("\\", "#"))  # Replaces special characters so that a text file can be created
    encrypted = str(encrypted.replace("|", "%"))  # Replaces special characters so that a text file can be created
    return encrypted  # Returns this string when the function is called

def decrypt(txt):  # Rotation Decryption function (5 backward alphabetical rotations) (THIS IS ONE OF THE COMPLEX ALGORITHMS)
    txt.replace('#', '\\')  # Replaces special characters so that the string can be decrypted
    txt.replace('%', '|')  # Replaces special characters so that the string can be decrypted
    decrypted = ''  # Clears string cache
    for x in txt:  # New loop (len of txt)
        c = ord(x) - 5  # Ord gets the ASCII value for a character and decreases its value by 5
        if ord(x) != c:  # If c is a new character
            b = chr(c)  # b equals the character of the ASCII value
            decrypted += b  # Adds each character to the encrypted string
    return decrypted  # Returns this string when the function is called

def welcome(): # Defines 'welcome()' function. This function will display an introduction to the program once an account has been created, giving details to the accont and a small explanation on what may be confusing.
    welcomeWindow = Tk() # Create tk root widget under the name 'welcomeWindow' to create the GUI interaction window
    welcomeWindow.geometry("1920x1080") # Sets the resolution of the window to '1920x1080'
    welcomeWindow.title("WELCOME_WINDOW") # Gives the window the title 'WELCOME_WINDOW'
    Label(welcomeWindow, text="Your account has been created, " + userName + "!""\n\n Your Login Email is: " + userEmail + "\nYour Master Password is: " + userPincode + "\n\nYou have been given 3 default apps: \n- " + emailData.capitalize() + "\n- Code Avengers\n- Python Turtle\nThe default passwords for these are: 'undefined', you can change this in the 'Change an existing password' menu setting.\n", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    Label(welcomeWindow, text="Once you have recorded your account details, press the 'Confirm' button below. Enjoy!", font=("Arial", 14)).pack() # Creates a label widget with text in the font 'Arial 14', as well as fit the size of the window to this label with '.pack()'
    Button(welcomeWindow, text="Confirm", command=startMenu, font=("Arial", 12)).pack() # Creates a button that, when pressed, calls the 'startMenu' function
    welcomeWindow.mainloop() # Event loop that allows the GUI interaction window to appear

startMenu()  # Starts the program