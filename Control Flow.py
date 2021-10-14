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