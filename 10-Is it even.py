"""
Exercise 10: Is it even? - 35 Marks
"""


def even(number): #function for even
    return number % 2 == 0 #if the number is devisible by 2 and remainder is 0 
def odd(number): #fuction for odd
    return number % 2 == 1 #if the number is devisible by 2 and remainder is 1
def main():
    number= int(input("Enter a number: ")) #asks user for a number

    if even(number): #If remainder is 0 it is even
        print("The number you have entered is EVEN")
    elif odd(number): #if remainder is 1 it is odd
        print("The number you have entered is ODD")
main()