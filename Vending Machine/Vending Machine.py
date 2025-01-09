"""
Vending Machine 
"""

"""
READ BEFORE RUNNING THE CODE

please keep your keyboard on CAPS 
"SINCE THIS VENDING MACHINE DOESNT ACCEPT LOWER CASE"

when you are asked to enter 1 or 0 
it meants yes or no
I just based it of on bool because I want to

please input the correct input

when you're in the checkout
you don't have to put a currency (Ex: AED or $)
just putting a number (Ex: 100 or 10.00)
"""

import sys,time #import so I can use it

def print_slow(str): #function so that everytime I print_slow("") it will print the letters slowly
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(3./90) #the speed of how fast the letter is supposed to appear (0.033 seconds so it goes a bit slower)

import pygame #pip install pygame <--- if you run the code and the music doesn't play then type this in the console
pygame.mixer.init()
pygame.mixer.music.load('C:\\Users\\Rhayne Tugade\\Desktop\\Vending Machine\\Dreaming_Injection.mp3')
pygame.mixer.music.play(loops=-1) #infinite loop until it stops at the end

#Dictionary for all the items in the Vending Machine
items = {
    'A1':{'name': 'Canned Monster Energy Drink Taurine + Ginseng', 'price': 3.50},
    'A2':{'name': 'Canned Monster Energy Cafe Latte', 'price': 3.50},
    'A3':{'name': 'Canned Monster Energy Loca Moca', 'price': 3.50},
    'A4':{'name': 'Canned Pepsi', 'price': 4.50},
    'A5':{'name': 'Canned Coke', 'price': 4.00},
    'B1':{'name': 'Water Bottle', 'price': 2.75},
    'B2':{'name': 'Bottled Coke', 'price': 3.50},
    'B3':{'name': 'Bottled Pepsi', 'price': 4.00},
    'C1':{'name': 'Lays Cheese', 'price': 5.70},
    'C2':{'name': 'Lays Salted', 'price': 6.00},
    'C3':{'name': 'Lays BBQ', 'price': 5.50},
    'C4':{'name': 'Doritos Nacho Cheese', 'price': 5.50},
    'C5':{'name': 'Doritos Spicy Nacho', 'price': 6.00},
    'C6':{'name': 'Doritos BQQ', 'price': 6.55},
    'C7':{'name': 'Cheetos Cheese', 'price': 5.45},
    'C8':{'name': 'Cheetos Cheddar Jalapeno', 'price': 4.85},
    'D1':{'name': 'Hersheys Bar', 'price': 4.75},
    'D2':{'name': 'Ferrero Bar', 'price': 6.50},
    'D3':{'name': 'Snicekers Bar', 'price': 5.45},
    'D4':{'name': 'M&M', 'price': 3.75}}

Filter_List = ['DRINKS', 'CHIPS', 'CHOCOLATE'] #Just a list for the filtering choices

#Dictionary for the Drinks only
Drinks = {
    'A1':{'name': 'Canned Monster Energy Drink Taurine + Ginseng', 'price': 3.50},
    'A2':{'name': 'Canned Monster Energy Cafe Latte', 'price': 3.50},
    'A3':{'name': 'Canned Monster Energy Loca Moca', 'price': 3.50},
    'A4':{'name': 'Canned Pepsi', 'price': 4.50},
    'A5':{'name': 'Canned Coke', 'price': 4.00},
    'B1':{'name': 'Water Bottle', 'price': 2.75},
    'B2':{'name': 'Bottled Coke', 'price': 3.50},
    'B3':{'name': 'Bottled Pepsi', 'price': 4.00}}

#Dictonary for the Chips only
Chips = {
    'C1':{'name': 'Lays Cheese', 'price': 5.70},
    'C2':{'name': 'Lays Salted', 'price': 6.00},
    'C3':{'name': 'Lays BBQ', 'price': 5.50},
    'C4':{'name': 'Doritos Nacho Cheese', 'price': 5.50},
    'C5':{'name': 'Doritos Spicy Nacho', 'price': 6.00},
    'C6':{'name': 'Doritos BQQ', 'price': 6.55},
    'C7':{'name': 'Cheetos Cheese', 'price': 5.45},
    'C8':{'name': 'Cheetos Cheddar Jalapeno', 'price': 4.85}}

#Dictionary for the Chocolates only
Chocolate ={
    'D1':{'name': 'Hersheys Bar', 'price': 4.75},
    'D2':{'name': 'Ferrero Bar', 'price': 6.50},
    'D3':{'name': 'Snicekers Bar', 'price': 5.45},
    'D4':{'name': 'M&M', 'price': 3.75}}

#I did this to make the design in the console a bit prettier and clean
print("\n\n\n\n-----------------------------------------------------------------------")
print_slow("\n\n                            Vending Machine                             ")
print("\n\n-----------------------------------------------------------------------")
print_slow("\n         Welcome USER! What would you like from the vending machine?")
print("\n-----------------------------------------------------------------------")

#to print the vending machine items
for key, item in items.items():
    print(f"    |  {key}  | {item['name']}- AED {item['price']}") 


print("\n-----------------------------------------------------------------------")
print_slow("\n                 Do you want to filter out the choices? ")
Filter= str(input("\n\n                                1 or 0: " )) #User input 1 is yes - 0 is no , I based this off on bool
if Filter== "1": #if the user types 1 which is yes
    print("\n-----------------------------------------------------------------------")
    print_slow("\nChoose what you want to filter?") #it will ask you which you want filtered which is the | DRINKS | CHIPS | CHOCOLATE |
    print("\n")
    print(*Filter_List, sep = '    |    ') #This one prints the list of choices of what the user wants to filter
    print("\n\n-----------------------------------------------------------------------")
    Chosen_Fil= str(input("\nEnter your chosen filter here: ")) #user input for when you choose
    print("\n-----------------------------------------------------------------------")
    if Chosen_Fil == "DRINKS": #If the user chooses to only see the drinks menu
        for key, item in Drinks.items(): 
            print(f"    |  {key}  | {item['name']}- AED {item['price']}") #it will print out just the drinks menu from the dictionary
        print("\n-----------------------------------------------------------------------")
        
        Code= str(input("                        Enter the code here: ")) #User input for the code when they're ready to choose what they want
        
        print_slow("\n                              L O A D I N G")
        
        print("\n-----------------------------------------------------------------------")
        
        if Code in items: #If the code the user inputs is within the dictionary
            selected_item= items[Code] #Variable for the selected code
            print_slow(f"\nYou have Successfully Added a {selected_item['name']}!!!")
            Price= selected_item['price'] #Variable for the selected items price
            print("\n-----------------------------------------------------------------------")
            while Price > 0: 
                try:
                    user_payment = float(input(f"\nPlease insert AED {Price:.2f}: ")) #.2f is so that it also includes the two decimals in the price
                    if user_payment >= Price: #If the users payment is greater than the price
                        change = user_payment - Price #varibale for computing the change which is whatever the users payment is minus the price of the chosen item
                        print("\n-----------------------------------------------------------------------")
                        print_slow("\n                      C O U N T I N G  P A Y M E N T")
                        print("\n-----------------------------------------------------------------------")
                        print_slow(f"\nYou have successfully purchased a {selected_item['name']}!")
                        print("\n-----------------------------------------------------------------------")
                        print_slow("\n                       Thank you for your purchase!")
                        print_slow(f"\n\n                         Your change is AED {change:.2f}")
                        print("\n-----------------------------------------------------------------------")
                        print_slow("\n                          Enjoy Your Purchase!!!!")
                        break
                    else: #If the payment of the user isn't enough, it will have you enter money again
                        print("\n-----------------------------------------------------------------------")
                        print_slow("\n                      C O U N T I N G  P A Y M E N T")
                        print("\n-----------------------------------------------------------------------")
                        print_slow("Insufficient payment. Please insert more money.")
                        print("\n-----------------------------------------------------------------------")
                        Price -= user_payment
                except ValueError: #If you don't put in numbers then it will be an error
                    
                    print_slow("Invalid payment amount. Please enter a valid number.")
        else: #If the user inputs a code that doesn't exist it will be invalid and will stop the whole thing
            
            print_slow("\n                   Invalid Code. Please try again.")
            print("\n-----------------------------------------------------------------------")
    elif Chosen_Fil == "CHIPS": #If the user chooses to only see the chips in the menu
        for key, item in Chips.items(): #It will print out the Chips dictionary
            print(f"    |  {key}  | {item['name']}- AED {item['price']}")
        print("\n-----------------------------------------------------------------------")
        
        Code= str(input("                        Enter the code here: "))
        
        print_slow("\n                              L O A D I N G")
        
        print("\n-----------------------------------------------------------------------")
        
        if Code in items:
            selected_item= items[Code]
            print(f"\nYou have Successfully Added a {selected_item['name']}!!!")
            Price= selected_item['price']
            print("\n-----------------------------------------------------------------------")
            while Price > 0:
                try:
                    user_payment = float(input(f"\nPlease insert AED {Price:.2f}: "))
                    if user_payment >= Price:
                        change = user_payment - Price
                        print("\n-----------------------------------------------------------------------")
                        print_slow("\n                      C O U N T I N G  P A Y M E N T")
                        print("\n-----------------------------------------------------------------------")
                        print_slow(f"\nYou have successfully purchased a {selected_item['name']}!")
                        print("\n-----------------------------------------------------------------------")
                        print_slow("\n                       Thank you for your purchase!")
                        print_slow(f"\n\n                         Your change is AED {change:.2f}")
                        print("\n-----------------------------------------------------------------------")
                        print_slow("\n                          Enjoy Your Purchase!!!!")
                        break
                    else:
                        print("\n-----------------------------------------------------------------------")
                        print_slow("\n                      C O U N T I N G  P A Y M E N T")
                        print("\n-----------------------------------------------------------------------")
                        print_slow("Insufficient payment. Please insert more money.")
                        print("\n-----------------------------------------------------------------------")
                        Price -= user_payment
                except ValueError:
                    
                    print_slow("Invalid payment amount. Please enter a valid number.")
        else:
            
            print_slow("\n                   Invalid Code. Please try again.")
            print("\n-----------------------------------------------------------------------")     
    elif Chosen_Fil == "CHOCOLATE": #If the user chooses the chocolate filter
        for key, item in Chocolate.items(): #It will only print the chocolate dictionary
            print(f"    |  {key}  | {item['name']}- AED {item['price']}")
        print("\n-----------------------------------------------------------------------")
        
        Code= str(input("                        Enter the code here: "))
        
        print_slow("\n                              L O A D I N G")
        
        print("\n-----------------------------------------------------------------------")
        
        if Code in items:
            selected_item= items[Code]
            print_slow(f"\nYou have Successfully Added a {selected_item['name']}!!!")
            Price= selected_item['price']
            print("\n-----------------------------------------------------------------------")
            while Price > 0:
                try:
                    user_payment = float(input(f"\nPlease insert AED {Price:.2f}: "))
                    if user_payment >= Price:
                        change = user_payment - Price
                        print("\n-----------------------------------------------------------------------")
                        print_slow("\n                      C O U N T I N G  P A Y M E N T")
                        print("\n-----------------------------------------------------------------------")
                        print_slow(f"\nYou have successfully purchased a {selected_item['name']}!")
                        print("\n-----------------------------------------------------------------------")
                        print_slow("\n                       Thank you for your purchase!")
                        print_slow(f"\n\n                         Your change is AED {change:.2f}")
                        print("\n-----------------------------------------------------------------------")
                        print_slow("\n                          Enjoy Your Purchase!!!!")
                        break
                    else:
                        print("\n-----------------------------------------------------------------------")
                        print_slow("\n                      C O U N T I N G  P A Y M E N T")
                        print("\n-----------------------------------------------------------------------")
                        print_slow("Insufficient payment. Please insert more money.")
                        print("\n-----------------------------------------------------------------------")
                        Price -= user_payment
                except ValueError:
                    
                    print_slow("Invalid payment amount. Please enter a valid number.")
        else:
            
            print_slow("\n                   Invalid Code. Please try again.")
            print("\n-----------------------------------------------------------------------")
    else:
        print_slow("\n                             Invalid Request")
        print("\n-----------------------------------------------------------------------")
elif Filter== "0":
    print("\n-----------------------------------------------------------------------")
    print_slow("\n              Choose what you want from the vending machine")
    print("\n-----------------------------------------------------------------------")
    for key, item in items.items():
        print(f"    |  {key}  | {item['name']}- AED {item['price']}")
    print("\n-----------------------------------------------------------------------")
    
    Code= str(input("                        Enter the code here: "))
    
    print_slow("\n                              L O A D I N G")
    
    print("\n-----------------------------------------------------------------------")
    
    if Code in items:
        selected_item= items[Code]
        print_slow(f"\nYou have Successfully Added a {selected_item['name']}!!!")
        Price= selected_item['price']
        print("\n-----------------------------------------------------------------------")
        while Price > 0:
            try:
                user_payment = float(input(f"\nPlease insert AED {Price:.2f}: "))
                if user_payment >= Price:
                    change = user_payment - Price
                    print("\n-----------------------------------------------------------------------")
                    print_slow("\n                      C O U N T I N G  P A Y M E N T")
                    print("\n-----------------------------------------------------------------------")
                    print_slow(f"\nYou have successfully purchased a {selected_item['name']}!")
                    print("\n-----------------------------------------------------------------------")
                    print_slow("\n                       Thank you for your purchase!")
                    print_slow(f"\n\n                         Your change is AED {change:.2f}")
                    print("\n-----------------------------------------------------------------------")
                    print_slow("\n                          Enjoy Your Purchase!!!!")
                    break
                else:
                    print("\n-----------------------------------------------------------------------")
                    print_slow("\n                      C O U N T I N G  P A Y M E N T")
                    print("\n-----------------------------------------------------------------------")
                    print_slow("Insufficient payment. Please insert more money.")
                    print("\n-----------------------------------------------------------------------")
                    Price -= user_payment
            except ValueError:
                
                print_slow("Invalid payment amount. Please enter a valid number.")
    else:
        
        print_slow("\n                   Invalid Code. Please try again.")
        print("\n-----------------------------------------------------------------------")
    
else: #If the user inputs something else other than a 1 or 0 it will be invallid and stop the code
    print("\n-----------------------------------------------------------------------")
    print_slow("\n                             Invalid Request")
    print("\n-----------------------------------------------------------------------")
    
pygame.mixer.music.stop() #Code so the music will stop