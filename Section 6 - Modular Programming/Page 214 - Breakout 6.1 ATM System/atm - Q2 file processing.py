# ATM System
# Menu driven program handle balance enuiries, lodgements, and withdrawals
# Q2 - Add functions to read and write balance from a file atm.txt

# A function to display the menu
def displayMenu():
    print("\t LCCS BANK LIMITED")
    print("\t ATM Main Menu")
    print("")
    print("\t(1) Balance Enquiry")
    print("\t(2) Cash Lodgement")
    print("\t(3) Cash Withdrawal")
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
            if (choice >= 0) and (choice < 4):
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

    bankFile.close()

# A function to write balance to the file
def writeATMFile():
    global balance, pin
    
    with open('atm.txt', 'w') as bankFile:
        bankFile.write(str(balance))
        bankFile.write("\n")



# Main processing
balance = 0.0
print("Balance is %.2f" %balance)

# Q2 Add a line to read atm.txt
readATMFile()

displayMenu()
menuOption = getChoice()
while menuOption != 0:
    if menuOption == 1:
        print("Balance is %.2f" %balance)
    elif menuOption == 2:
        amount = float(input("How much do you want to lodge? "))
        processLodgement(amount)
    elif menuOption == 3:
        amount = float(input("How much do you want to withdraw? "))
        processWithdrawal(amount)

    displayMenu()
    menuOption = getChoice()


# Q2 Add a line to write atm.txt
writeATMFile()

print("Thank you for banking with LCCS BANK LIMITED")
print("Balance is %.2f" %balance)


