# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 23:05:22 2022

@author: Patrick Jordan
"""
from termcolor import colored
import random

def tryRest(numberOfTries, computerValue):
    if(tries>0): 
        print("It is not correct try again! You have ",numberOfTries," another tries!")
    else:
        print("Sorry it was your last chance! You lost!")
        print("The word was: ", computerValue)

def verify(a,b):
    for i in range(len(a)):
        if(a[i]==b[i]):
            print(colored(a[i],'green'))
        else:
            print(colored(a[i],'red')) 

with open("five_letters_words.txt","r+") as file:
#print(file.readlines())
    five_List = file.readlines()
    file.close()
   
for i in range (len(five_List)):
   five_List[i]=five_List[i][0:5]

computerValue="A"  #initialisierung der zwei Variablen
userValue="B" 
tries=10
   
computerValue=random.choice(five_List)
#print(computerValue)
while((computerValue!=userValue) and(tries>0)):
    tries=tries-1
    userValue=input("Geben Sie etwas an!")
    if(userValue==computerValue):
        verify( userValue, computerValue)
        print(True)
        print("Congratulations, You found the fire word!")
    else:
        if (len(userValue)!=5)  :
            print("The word must have 5 letters\n")
            tryRest(tries,computerValue)
        else:
            verify( userValue, computerValue)
            tryRest(tries, computerValue)
   
