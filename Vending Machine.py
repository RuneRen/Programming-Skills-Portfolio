"""
Vending Machine 
"""


import sys,time #Just for fun, so that the words slow down a bit when printing

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(3./90)

import pygame #pip install pygame 
pygame.mixer.init()
pygame.mixer.music.load('C:\\Users\\Rhayne Tugade\\Desktop\\Vending Machine\\DreamingInjection.mp3')
pygame.mixer.music.play()

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
    'C4':{'name': 'Doritos Nacho Chese', 'price': 5.50},
    'C5':{'name': 'Doritos Spicy Nacho', 'price': 6.00},
    'C6':{'name': 'Doritos BQQ', 'price': 6.55},
    'C7':{'name': 'Cheetos Cheese', 'price': 5.45},
    'C8':{'name': 'Cheetos Cheddar Jalapeno', 'price': 4.85},
    'D1':{'name': 'Hersheys Bar', 'price': 4.75},
    'D2':{'name': 'Ferrero Bar', 'price': 6.50},
    'D3':{'name': 'Snicekers Bar', 'price': 5.45},
    'D4':{'name': 'M&M', 'price': 3.75}}

Filter_List = ['Drinks', 'Chips', 'Chocolate'] #Just a list for the filtering choices

#Dictionary for the Drinks
Drinks = {
    'A1':{'name': 'Canned Monster Energy Drink Taurine + Ginseng', 'price': 3.50},
    'A2':{'name': 'Canned Monster Energy Cafe Latte', 'price': 3.50},
    'A3':{'name': 'Canned Monster Energy Loca Moca', 'price': 3.50},
    'A4':{'name': 'Canned Pepsi', 'price': 4.50},
    'A5':{'name': 'Canned Coke', 'price': 4.00},
    'B1':{'name': 'Water Bottle', 'price': 2.75},
    'B2':{'name': 'Bottled Coke', 'price': 3.50},
    'B3':{'name': 'Bottled Pepsi', 'price': 4.00}}

#Dictonary for the Chips
Chips = {
    'C1':{'name': 'Lays Cheese', 'price': 5.70},
    'C2':{'name': 'Lays Salted', 'price': 6.00},
    'C3':{'name': 'Lays BBQ', 'price': 5.50},
    'C4':{'name': 'Doritos Nacho Chese', 'price': 5.50},
    'C5':{'name': 'Doritos Spicy Nacho', 'price': 6.00},
    'C6':{'name': 'Doritos BQQ', 'price': 6.55},
    'C7':{'name': 'Cheetos Cheese', 'price': 5.45},
    'C8':{'name': 'Cheetos Cheddar Jalapeno', 'price': 4.85}}

#Dictionary for the Chocolates
Chocolate ={
    'D1':{'name': 'Hersheys Bar', 'price': 4.75},
    'D2':{'name': 'Ferrero Bar', 'price': 6.50},
    'D3':{'name': 'Snicekers Bar', 'price': 5.45},
    'D4':{'name': 'M&M', 'price': 3.75}}


print("\n\n\n\n-----------------------------------------------------------------------")
print_slow("\n\n                            Vending Machine                             ")
print("\n\n-----------------------------------------------------------------------")
print_slow("\n         Welcome USER! What would you like from the vending machine?")
print("\n-----------------------------------------------------------------------")


for key, item in items.items():
    print(f"    |  {key}  | {item['name']}- AED {item['price']}") 

print("\n-----------------------------------------------------------------------")
print_slow("\n                 Do you want to filter out the choices? ")
Filter= str(input("\n\n                                1 or 0: " ))
if Filter== "1":
    print("\n-----------------------------------------------------------------------")
    print_slow("\nChoose what you want to filter?")
    print("\n")
    print(*Filter_List, sep = '    |    ')
    print("\n\n-----------------------------------------------------------------------")
    Chosen_Fil= str(input("\nEnter your chosen filter here: "))
    print("\n-----------------------------------------------------------------------")
    if Chosen_Fil == "Drinks":
        for key, item in Drinks.items():
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
    elif Chosen_Fil == "Chips":
        for key, item in Chips.items():
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
    elif Chosen_Fil == "Chocolate":
        for key, item in Chocolate.items():
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
    
else:
    print("\n-----------------------------------------------------------------------")
    print_slow("\n                             Invalid Request")
    print("\n-----------------------------------------------------------------------")
    
pygame.mixer.music.stop()