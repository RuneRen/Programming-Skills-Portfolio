"""

EXERCISE 4: PRIMITIVE QUIZ - 30 MARKS
*************************************

"""

Score= 0 #keeps track of your score
Final_Score= Score
F=str(input("1. What is the capital of France? ")) #question
if F <= "Paris" or "paris" or "PARIS":
    print ("Your answer is correct")
    Score +=1 #adds 1 to your score

else:
    print("Your answer is wrong")
    
G=str(input("2. What is the capital of Germany? "))
if G <= "Berlin" or "berlin" or "BERLIN":
    print ("Your answer is correct")
    Score +=1 #adds 1 to your score

else:
    print("Your answer is wrong")
    
I=str(input("3. What is the capital of Italy? ")) 
if I <= "Rome" or "rome" or "ROME":
    print ("Your answer is correct")
    Score +=1 #adds 1 to your score

else:
    print("Your answer is wrong")

UK=str(input("4. What is the capital of United Kingdom? ")) 
if UK <= "London" or "london" or "LONDON":
    print ("Your answer is correct")
    Score +=1 #adds 1 to your score

else:
    print("Your answer is wrong")

RU=str(input("5. What is the capital of Russia? ")) 
if RU <= "Moscow" or "moscow" or "MOSCOW":
    print ("Your answer is correct")
    Score +=1 #adds 1 to your score

else:
    print("Your answer is wrong")

ARM=str(input("6. What is the capital of Armenia? ")) 
if ARM <= "Yerevan" or "yerevan" or "YEREVAN":
    print ("Your answer is correct")
    Score +=1 #adds 1 to your score
 
else:
    print("Your answer is wrong")
    
S=str(input("7. What is the capital of Spain? ")) 
if S <= "Madrid" or "madrid" or "MADRID":
    print ("Your answer is correct")
    Score +=1 #adds 1 to your score
\
else:
    print("Your answer is wrong")

NL=str(input("8. What is the capital of Netherlands? ")) 
if NL <= "Amsterdam" or "amsterdam" or "AMSTERDAM":
    print ("Your answer is correct")
    Score +=1 #adds 1 to your score

else:
    print("Your answer is wrong")
    
George=str(input("9. What is the capital of Georgia? ")) 
if George <= "Tbilisi" or "tbilisi" or "TBILISI":
    print ("Your answer is correct")
    Score +=1 #adds 1 to your score

else:
    print("Your answer is wrong")
    
ROM=str(input("10. What is the capital of Romania? ")) 
if ROM <= "Bucharest" or "bucharest" or "BUCHAREST":
    print ("Your answer is correct")
    Score +=1 #adds 1 to your score

else:
    print("Your answer is wrong")
    
print("Congratulations, your score is" + " " +str(Score) + " " +"out of 10 questions.") #prints out the score you got out of the 10 questions.
















