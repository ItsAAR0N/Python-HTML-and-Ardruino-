# A PROGRAM WHICH LETS YOU ADD ITEMS TO A WEEKLY SHOPPING LIST
# PROGRAM BY AARON S.

#  $$$$$$\                                                 $$$$$$\      
# $$  __$$\                                               $$  __$$\     
# $$ /  $$ | $$$$$$\   $$$$$$\   $$$$$$\  $$$$$$$\        $$ /  \__|    
# $$$$$$$$ | \____$$\ $$  __$$\ $$  __$$\ $$  __$$\       \$$$$$$\      
# $$  __$$ | $$$$$$$ |$$ |  \__|$$ /  $$ |$$ |  $$ |       \____$$\     
# $$ |  $$ |$$  __$$ |$$ |      $$ |  $$ |$$ |  $$ |      $$\   $$ |    
# $$ |  $$ |\$$$$$$$ |$$ |      \$$$$$$  |$$ |  $$ |      \$$$$$$  |$$\ 
# \__|  \__| \_______|\__|       \______/ \__|  \__|       \______/ \__|

# IMPORT

import time as t # TIME (SLEEP)
import numpy 

# USER INPUT
print("Welcome, would you like to add to your shopping list? ")

# I
# .NPUT VALIDATION
while True:
    user_input = (str(input("(y/n): "))).lower()
    while user_input != "y" and user_input != "n": # IF USER_INPUT NOT (y/n)
        try:
            user_input(str("Error, must be (y/n) "))
            break
        except: 
            print("Error! Must be (y/n) ")
            break
    if user_input == "n":
        print("Closing program...")
        t.sleep(1)
        raise SystemExit
        break   
    elif user_input == "y":
        print("Okay, moving on...")
        t.sleep(1)
        break

# INPUT VALIDATION (INT)
while True:
    try:
        no_of_items = (int(input("How many items would you like to add to the list? ")))
        break
    except ValueError:
        print("Error! Must be integer only")

# USER INPUT

print("Please enter the item(s): ")
# ARRAY (PY.LIST)

shoppinglist = [] # ASSIGN VARIABLE AS A 1D ARRAY
for i in range(no_of_items):
    item = (str(input("")))
    shoppinglist.append(item)
    
print("This is your current shopping list: ")
# ENUMERATION
for number, itemlist in enumerate(shoppinglist,start=1):
    print(str(number) + ".", str(itemlist))
# SPACE OUT
for x in range(3):
    print(".")
    t.sleep(1)

# USER INPUT 
input_user = (str(input("Would you like to make ammendments, add, delete or close program? (amm / a / d / c): ")))
while input_user != "amm" and input_user != "a" and input_user != "d" and input_user != "c":
    try:
        print("Error, must be:")
        t.sleep(1)
        print("(amm) for AMMENDMENTS")
        t.sleep(1)
        print("(a) for ADD Item(s)")
        t.sleep(1)
        print("(d) for DELETE Item(s)")
        t.sleep(1)
        print("(c) for CLOSE program")
        t.sleep(1)
        input_user = (str(input("Would you like to make ammendments, add, delete or close program? (amm / a / d / c): ")))
        break
    # EXCEPTION MESSAGE    
    except:
        print("Error, must be amm, a, d or c!!")

# AMMENDMENTS. (change value)
if input_user == "amm": 
    print("Sure, please enter the no. of the item from the list: ")
    while True: 
        try:
            ammendment_no = (int(input(""))) 
            replaced_item = (str(input("Please enter: ")))
            shoppinglist[ammendment_no] = replaced_item  
            print("This is your new list now:")
            break            
        except ValueError:
            # EXCEPTION MESSAGE
                print("Error, must be integer only")
# PRINT 

    for number, itemlist in enumerate(shoppinglist,start=1):
        print(str(number) + ".", str(itemlist))
# ClOSE PROGRAM
    t.sleep(5)
    raise SystemExit
 
# ADD. (append)       
elif input_user == "a":
    print("Sure, how many items do you wish to add?")
    while True:
        try:
            add_count = (int(input("")))
            # USER INPUT
            print("Insert item.")     
            for i in range(add_count):
                add_item = (str(input("")))
                shoppinglist.append(add_item)
                print("This is your new list now:")
            break
        except ValueError:
            # EXCEPTION MESSAGE
            print("Error, must be integer only")
# PRINT    
    for number, itemlist in enumerate(shoppinglist,start=1):
        print(str(number) + ".", str(itemlist))
# ClOSE PROGRAM
    t.sleep(5)
    raise SystemExit

# DELETE. (pop)  

elif input_user == "d":
    print("Sure, please enter the no. of the item to delete from the list: ")
    while True:
        try:
            delete_item = (int(input(": ")))
            shoppinglist.pop(delete_item)
            print("This is your new list now")
            break        
        except ValueError:
            # EXCEPTION MESSAGE
            print("Error, must be integer only")
# PRINT 
    for number, itemlist in enumerate(shoppinglist,start=1):
        print(str(number) + ".", str(itemlist))
# ClOSE PROGRAM
    t.sleep(5)
    raise SystemExit

elif input_user == "c":
    print("Good day!")
    # ClOSE PROGRAM
    t.sleep(5)
    raise SystemExit

# [END OF CODE.]