# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 15:02:32 2020

@author: Aaron
"""

# Program to display stats from a video game, using classes as practice.

class KDratio: # Define class as KDratio
    def __init__(self, kills,deaths): # Special initialisation of variables 
        self.kills = kills
        self.deaths = deaths
        
    def DisplayStat(self): # Class to display stats
        print("\nKills:",self.kills)
        print("Deaths:",self.deaths)
        
    def CalcKD(self):        
        if deaths == 0: # Avoid DivByZero error
            print("\nYour K/D ratio is:\n{0}".format(self.kills))
        else:
            ratio = (self.kills)/(self.deaths)
            FinalRatio = round(ratio,2) # Round to two dec. 
            print("\nYour K/D ratio is:\n{0}".format(FinalRatio)) 

print("Program to calculate K/D ratio and display stats, use whole numbers only")

while True: # Ensure input values are whole numbers
    try:
        kills = (int(input("Please enter the amount of kills you obtained: "))) # Receive input from keyboard
        deaths = (int(input("Please enter the amount of deaths: ")))
        break
    except ValueError: # If val is not int
        print("Error, must be whole number.")
        
        
call = KDratio(kills,deaths) # Assign variables from keyboard as input parameters to the class

call.DisplayStat() # Call functions
call.CalcKD()

