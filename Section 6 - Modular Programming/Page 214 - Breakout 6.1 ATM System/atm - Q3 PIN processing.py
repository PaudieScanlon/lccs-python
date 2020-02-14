# ATM System
# Menu driven program handle balance enuiries, lodgements, and withdrawals
# Q3 - Add PIN processing

# A function to display the menu
def displayMenu():
    print("\t LCCS BANK LIMITED")
    print("\t ATM Main Menu")
    print("")
    print("\t(1) Balance Enquiry")
    print("\t(2) Cash Lodgement")
    print("\t(3) Cash Withdrawal")
    print("\t(4) Change PIN")
    print("")
    print("\t(0) Exit")
    print("")    

# A function to read and valididate the menu option
def getChoice():
    
    validChoice = False
    while not validChoice:
        choice = input("\t CHOOSE AN OPTION >> ")                
        if choice.isdigit():
            choice = int(choice)
            if (choice >= 0) and (choice <= 4):
                validChoice = True

    return choice


# A function to process withdrawals
def processWithdrawal(withdrawalAmount):
    global balance

    # Q1. Prevent withdrawals exceeding €200
    if withdrawalAmount > 200:
        print("The maximum withdrawal amount permitted is €200")
        return

    if (withdrawalAmount > balance):
        print("Insufficient Funds.")
    else:
        balance = balance - withdrawalAmount
        print("Please take your cash.")

    return

# A function to process lodgements
def processLodgement(lodgeAmount):
    global balance

    if (lodgeAmount%10 == 0):
        balance = balance + lodgeAmount
    else:
        print("Amounts must be a multiple of 10.")

    return


# A function to read the balance from the file
def readATMFile():
    global balance, pin
    
    bankFile = open("atm.txt", "r")
    balance = float(bankFile.readline())
    pin = int(bankFile.readline())
    bankFile.close()

# A function to write balance to the file
def writeATMFile():
    global balance, pin
    
    with open('atm.txt', 'w') as bankFile:
        bankFile.write(str(balance))
        bankFile.write("\n")
        bankFile.write(str(pin))

# This function returns a valid PIN
def getValidPIN(msg):

    validPIN = False
    
    while not validPIN:
        userPin = input(msg)
        if userPin.isdigit():
            userPin = int(userPin)
            if (userPin >= 0) and (userPin <= 9999):
                validPIN = True
    # is 12 a vaid PIN
    return userPin


# This function returns TRUE if the PIN entered matches the system PIN
# FALSE otherwise.
def isValidUser(currentPin):

    userPin = -1
    tries   =  0
    while ((userPin != currentPin) and (tries < 3)):
        userPin = getValidPIN("Enter your 4 digit PIN >> ")
        tries  =  tries+1

    if (userPin == currentPin):
        return True
    else:
        return False


# This function returns TRUE if the user PIN was entered correctly. FALSE otherwise.
def changePin(oldPin):

    newPin1 = getValidPIN("Enter your new 4 digit PIN >> ")
    newPin2 = getValidPIN("Confirm your new 4 digit PIN >> ")    

    if (newPin1 == newPin2):
        return newPin1
    else:
        print("PIN mistmatch - change unsuccessful")
        return oldPin


# Main processing
balance = 0.0
pin = 0000
# Q2 Add a line to read atm.txt
readATMFile()

if isValidUser(pin):
    displayMenu()
    menuOption = getChoice()
    while menuOption != 0:
        if menuOption == 1:
            print("Balance is: %.2f" %balance)
        elif menuOption == 2:
            amount = float(input("How much do you want to lodge? "))
            processLodgement(amount)
        elif menuOption == 3:
            amount = float(input("How much do you want to withdraw? "))
            processWithdrawal(amount)
        elif menuOption == 4:
            pin = changePin(pin)

        displayMenu()
        menuOption = getChoice()

    writeATMFile()
    print("Thank you for banking with LCCS BANK LIMITED")
    print("Balance is: %.2f" %balance)
else:
    print("Invalid PIN. Access denied")
