# A PROGRAM WHICH DETERMINES WHETHER OR NOT YOU CAN MAKE A CAKE BASED UPON THE INGREDIENTS YOU HAVE ALREADY.
# GLOBAL VARIABLES

#   /$$$$$$                                             
#  /$$__  $$                                              
# | $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$  
# | $$$$$$$$ |____  $$ /$$__  $$ /$$__  $$| $$__  $$
# | $$__  $$  /$$$$$$$| $$  \__/| $$  \ $$| $$  \ $$   
# | $$  | $$ /$$__  $$| $$      | $$  | $$| $$  | $$
# | $$  | $$|  $$$$$$$| $$      |  $$$$$$/| $$  | $$  
# |__/  |__/ \_______/|__/       \______/ |__/  |__/  
                                                                                                                          
                                                                                                                          

import webbrowser as wb # WEB FUNCTION

butter = ""
margarine = ""
caster_sugar = ""
eggs = ""
sr_flour = ""

print("Hello, this is a program to determine whether you can make spongecake right now or not.")

# USER PROMPT

user_input = str(input("Do you have margarine or butter, (y/n): ")).lower()
if user_input =="n":
    print("Go get butter or margerine first! Then come back.")
    raise SystemExit

while user_input != "y" and user_input != "n": 
   
        user_input = str(input("Please only enter (y/n): ")).lower()
        if user_input == "y": 
            break
        elif user_input == "n":
            print("Go get butter or margarine first! Then come back.")
            raise SystemExit
 
# EXPECTING USER INPUT        

while True:
    try:
        butter = int(input("How much butter do you have (g): "))
        margarine = int(input("How much margarine do you have (g): "))
        caster_sugar = int(input("How much caster sugar do you have (g): "))
        eggs = int(input("How many eggs do you have? "))
        sr_flour = int(input("How many grams of 'self-raising' flour do you have? "))
        break
    except:
        print("It must be an integer only! Program restarting...")

# COMPARISON

while butter > 125 and margarine > 125 and caster_sugar > 125 and eggs > 2 and sr_flour > 125:
    print("Congrats! You have enough to create a cake right now!")
    user_response = str(input("Do you want a list of instructions of how to make a cake? (y/n): ")).lower()
    if user_response == "y":
        wb.open_new_tab('http://www.bbc.co.uk/food/recipes/spongecake_1284'); # OPENS UP A NEW WEBSITE
        print("Have a nice day!")
        raise SystemExit
    if user_response == "n":
        print("Okay! Have a nice day! :)")
        raise SystemExit

       
# SETTING STRING VARIABLES SO IT IS EASIER TO READ.

onemsg = " g... Go get more!"

# COMPARISONS

if butter < 125 or margarine < 125 or caster_sugar < 125 or eggs < 2 or sr_flour < 125:
    print("You don't have enough ingredients to create a cake as of now, you need the following ingredients:")
  
    if butter < 125:
        print("125g of butter. You only have " + str(butter) + str(onemsg))
    if margarine < 125:
            print("125g of margarine. You only have " + str(margarine) + str(onemsg))
    if caster_sugar < 125: 
            print("125g of caster sugar. You only have " + str(caster_sugar) + str(onemsg))
    if eggs < 2:
           print("2 eggs. You only have " + str(eggs))
    if sr_flour < 125:
            print("125g of SR flour. You only have " + str(sr_flour) + str(onemsg))
    
# [END OF CODE]

raise SystemExit