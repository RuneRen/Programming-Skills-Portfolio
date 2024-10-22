# -*- coding: utf-8 -*-
"""
Exercise 5: Days of the Month - 30 Marks
****************************************
"""
Months_and_Days = {1:31,
                  2:28,
                  3:31,
                  4:30,
                  5:31,
                  6:30,
                  7:31,
                  8:31,
                  9:30,
                  10:31,
                  11:30,
                  12:31}
#dictionary of the months and days
your_year=int(input("Enter the year: ")) #variable for the year the user inputs
month_number=int(input("Enter the month number: ")) #variable for the month the user inputs

def leap(year): #function to make my life easier
    if(year % 400 ==0) or (year % 4 ==0 and year %100 != 0): #to calculate the year
        return True
    return False
if leap(your_year): #checks if it's a leap year
    print("This is a leap year")
    if month_number not in Months_and_Days: #checks if the number is inside the dictionary
        print("Invalid month number") #if it's not inside the dictionary it prints this   
    else:
        if month_number == 2:
            print("There are", Months_and_Days[month_number] +1, "days in this month.") #since the month is february on a leap year we will add 1 more day to make it 29
        else: #if it is inside
            print("There are", Months_and_Days[month_number] , "days in this month.") #it will print out the days
else: #if it's not a leap year
    print("This is not a leap year") #it will print this out
    if month_number not in Months_and_Days:
        print("Invalid month number") #If it's not in the dictionary it will print this out
    else: #if it is inside the dictionary
        print("There are", Months_and_Days[month_number] , "days in this month.") #it will print this












