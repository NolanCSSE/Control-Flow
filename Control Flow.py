# Programmer: Nolan Loukes
# Date: 10/11/2021
# Program: ATM Bank Transaction

"""
This program simulates an ATM utilizing IF, Elif, & Else statements
Nesting If statements and refresh our Comparison & Logical Operators
"""

print("Welcome to Cash-R-Us,\nLet's take a moment to set up your account.\n")

# Set up account by asking Us Bank users for their first & last names using Variables
firstName = input("What is your first name: ")
lastName = input("What is your last name: ")

print("\nWelcome to Cash-R-Us",firstName,lastName + ", we will now set up a security pin on you account.\n")

# Set up PIN - Personal Identification Number
pin = input("Please choose a 4 digit Personal Identification Number: ")

print("\nThank you",firstName + ", we see that you set your PIN to",pin)

print("\nWould you like to make a transaction through our Automated Teller Machine")
atm = input("Yes or No: ").lower()

if atm == "yes":
    print("\n*****************************************************\n")

    # This part of the program will be asking users to complete a transaction through the ATM
    print("Please insert your ATM card")
    print("Welcome to Cas-R-Us ATM",firstName,lastName,"\n")
    userPIN = input("what is your four digit PIN: ")

    if pin == userPIN:
        balance = 20
        print("\nYour Balance: $" + str(balance))

        # Ask users what type of transaction they want - Withdrawal - Deposit
        typeOfTransaction = input("\nWould you like to make a Withdrawal, Deposit, or check your Balance\nW = Withdrawal - D = Deposit - B = Balance: ").lower()
        if typeOfTransaction == "w":
            withAmount = int(input("Enter amount of withdrawal: "))
            if withAmount > balance:
                print("So sorry, you don't have enough money to withdrawal that amount")
            else:
                balance = balance - withAmount
                print("Your new balance is: $" + str(balance))

        
        elif typeOfTransaction == "d":
            deAmount = int(input("Enter amount of deposit: "))
            balance = balance + deAmount
            print("Your new balance is: $" + str(balance))

        else:
            print("Your Current balance is: $" + str(balance))

    else:
        print("Sorry",firstName,lastName,"your PIN doesn't match our records")


else:
    print("\nHave a wonderful day",firstName,lastName + ", please come back and visit soon.")
