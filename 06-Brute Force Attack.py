# -*- coding: utf-8 -*-
"""
Exercise 6: Brute Force Attack - 30 Marks
*****************************************
"""

password= "12345" #Variable for the password
guesses="" #variable for what we guessed
attempts= 5 #max number of attempts

while attempts >0: #as long as our attempts are above 0 we can guess
    guess= input("Enter the password: ") #where we put our guesses
    if guess == password: #if we guess the password correctly
        print("Correct Password!") #it prints that it is correct
        break #stops
    else: #if we guess incorrectly
        attempts = attempts - 1 #it will lessen our attempts by 1
        print("Incorrect Password, you have", attempts, "attempts remaining")
        if attempts == 0: #when our attempts reaches 0 we cannot guess anymore
            print("You have made too many attempts, the authorities have been alerted.")