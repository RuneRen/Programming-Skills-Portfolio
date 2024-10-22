# -*- coding: utf-8 -*-
"""
Exercise 7: Some Counting - 20 Marks
************************************
"""
#Variables
i=0  
j=0
k=0
l=0
m=0

print("\nzero to fifty:")
for i in range(0,51): #will count up from 0 to 50
    print(i) 
    
print("\nfifty to zero:")
for j in reversed(range(0,51)): #will count down from 50 to 0
    print(j)
    
print("\nthirty to fifty:")
for k in range(30,51): #will count up from 30 to 50
    print(k)

print("\nfifty to ten:")
for l in reversed(range(10,51,2)): #will count down from 50 to 10 in decrements of 2
    print(l)
    
print("\none hundred to two hundred:") #will count up from 100 to 200 in increments of 5
for m in range(100,201,5):
    print(m)
