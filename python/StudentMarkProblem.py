# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 01:06:06 2021

@author: Aaron
"""

MarkTotal = 0
count = 0
studentFinished = ""

def Repeat(MarkTotal,count):
    Usr_Input = input("Do you wish to continue? (y): ").lower()
    if Usr_Input == "y":
        studentFinished = False
        return studentFinished 
    else:
        ClassAvg = (MarkTotal/count)
        print("The class average is: {0}%".format(round(ClassAvg)))
        studentFinished = True
        return studentFinished



while studentFinished != True:
    studentNo = int(input("Please enter how many students there are: "))
    for count in range(0,studentNo):
        count += 1
        studentMark = int(input("What is Student {0}'s mark? ".format(count)))
        localMark = ((studentMark/70)*100)
        MarkTotal += localMark
        if localMark > 50 and localMark < 90:
            print("Very well done.")
        elif localMark > 50:
            print("Excellent result.")
        else:
            print("Try harder next time.")
 
        if count == studentNo:
            Repeat(MarkTotal,count)
            

            
    