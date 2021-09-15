# A PROGRAM WHICH CALCULATES APPROVAL RATINGS (SIMPLE) 
# MADE BY AARON S. 
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

# USER INPUT 
print("Hello! I will calculate the approval rating for you.")
print(".")
t.sleep(1)
print(".")
t.sleep(1)
print(".")
t.sleep(1)

while True:
    try: 
        user_like_cnt = (int(input("Please input your like count: ")))
        user_dislike_cnt = (int(input("Please input your dislike count: ")))
        break
    except ValueError:
        print("Error, must be integer value only.")

# CALCULATION 

print("Calculating...")
t.sleep(2)
print("Your total like count is: " + str(user_like_cnt))
t.sleep(1)
print("Your total dislike count is: " + str(user_dislike_cnt))

# FORMULA
total_percentage = ((user_like_cnt)/((user_like_cnt) + (user_dislike_cnt))) * 100

print("The approval percentage is: " + str(round(total_percentage)) + "%")

t.sleep(3)
print("Have a nice day!")
raise SystemExit

# [END OF CODE.]