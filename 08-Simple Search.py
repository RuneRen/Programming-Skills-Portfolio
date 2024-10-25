# -*- coding: utf-8 -*-
"""
Exercise 8: Simple Search - 30 Marks
************************************
"""


my_list=["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] #the list of names
print("Objective: find the person we're looking for!! You have one attempt :D")
print(my_list)
search= str(input("Enter the name you think we're looking for': "))#have to look for sam but pretend you don't know it's Sam
if search == "Sam": #if the one we searched is Sam 
    print("Congratulations, you have found Sam") #it will print that we have found Sam
else: #if it's not Sam
    print("This person is not the one we're looking for") #it will let us know that we looked for the wrong one