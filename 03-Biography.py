"""

EXERCISE 3: BIOGRAPHY - 25 MARKS
********************************

"""



information = {'first_name': str(input("Enter your first name: ")),
           'last_name': str(input("Enter your last name: ")),
           'hometown': str(input("Enter your hometown: ")),
           'age': str(input("Enter your age: "))} 

"""
asks for your input and stores the information you put in
as key-value pairs in a dictionary

I used a string for 'age' too so that the user 
can either put "16" or "sixteen".
"""
print("\nYour Information: ")
for value in information.values(): #Selects only values
    print(value) #prints all the values
    
#Advanced Requirement
print("\nYour name is" + " "  + information['first_name']+ " " +information['last_name'] + ".")
#Your name is 'first_name' 'last_name'.
print("Your hometown is in " + " " + information['hometown'] + ".")
#Your hometown is in _____.
print("You are" + " " + information['age'] + " " +" years old.")
#You are ___ years old.

