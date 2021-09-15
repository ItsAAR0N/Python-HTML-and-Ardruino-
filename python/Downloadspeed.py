# A PROGRAM WHICH CALCULATES DOWNLOAD TIME OF A FILE.
# PROGRAM BY AARON S.

#   /$$$$$$                                            
#  /$$__  $$                                         
# | $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$
# | $$$$$$$$ |____  $$ /$$__  $$ /$$__  $$| $$__  $$ 
# | $$__  $$  /$$$$$$$| $$  \__/| $$  \ $$| $$  \ $$
# | $$  | $$ /$$__  $$| $$      | $$  | $$| $$  | $$
# | $$  | $$|  $$$$$$$| $$      |  $$$$$$/| $$  | $$
# |__/  |__/ \_______/|__/       \______/ |__/  |__/
                                                                                                                                   
# IMPORT

import webbrowser as wb # IMPORT WEB MODULE
import time as t


# INITIALISING GLOBAL VARIABLES AS INT

wifi_speed = ""
file_size = ""
download_time = ""
time_factor = ""
total_time = ""

print("Hello, this program will be able to tell you the time :p")

user_input = str(input("Do you know your download speed already? (y/n): ")).lower()
if user_input == "y":
    print("Great! We can move on!")
elif user_input == "n":
    print("Okay... Go get your internet download speed from the website, and insert here: ")
    wb.open_new_tab('http://speedtest.net') # OPENS UP A NEW BROWSER

# INPUT VALIDATION

while user_input != "y" and user_input != "n":
    user_input = (str(input("Error, must be (y/n): "))).lower()
    if user_input == "y":
        print("Great! We can move on!")
        break
    elif user_input == "n":
        print("Okay... Go get your internet download speed from the website,")
        wb.open_new_tab('http://speedtest.net') # OPENS UP A NEW BROWSER

# USER INPUT

while True:
    try:       
        wifi_speed = (int(input("Please insert your WiFi download speed. (Mbps): ")))
        file_size = (int(input("Please insert the file size. (GB): ")))
        break
    except:
        print("It must be an integer only! Restarting...")

print("Are you happy with your values?")
print(str(wifi_speed) + " Mbps")
print(str(file_size) + " GB")

# USER INPUT

yes_no = str(input("(y/n): ")).lower()
if yes_no == "y":
    print("Okay! Now calculating...")
elif yes_no == "n":
    wifi_speed = (int(input("Please insert your WiFi download speed. (Mbps): ")))
    file_size = (int(input("Please insert the file size. (GB): ")))
    print("Your values are:")
    print(str(wifi_speed) + " Mbps")
    print(str(file_size) + " GB")
    print("Now calculating...")

# INPUT VALIDATION

while yes_no != "y" and yes_no !="n":
    yes_no = (str(input("Error, must be (y/n):"))).lower()
    if yes_no == "y":
        print("Now calculating...")
        break
    elif yes_no == "n":
        while True:
            try:
                wifi_speed = (int(input("Please insert your WiFi download speed. (Mbps): ")))
                file_size = (int(input("Please insert the file size. (GB): ")))
                print("Your values are:")
                print(str(wifi_speed) + " Mbps")
                print(str(file_size) + " GB")
                print("Now calculating...")
                break
            except:
                print("It must be an integer only! Restarting...")


time_format = (str(input("What time format would you like it in? (sec/min/hr): ")))
if time_format == "sec":
    time_factor = 1
    time = "secs"
elif time_format == "min":
    time_factor = 60
    time = "mins"
elif time_format == "hr":
        time_factor = 3600
        time = "hrs"

# INPUT VALIDATION

while time_format != "sec" and time_format != "min" and time_format != "hr":
    time_format = (str(input("Error, must be sec, min or hr only: ")))
    while time_format == "sec" or time_format == "min" or time_format == "hr":
        try:
            if time_format == "sec":
                time_factor = 1
                time = "secs"
                break
            elif time_format == "min":
                    time_factor = 60
                    time = "mins"
                    break
            elif time_format == "hr":
                        time_factor = 3600
                        time = "hrs"
                        break
        except:
               print("It must only be sec, mins or hr!")

# FINAL CALCULATIONS

download_speed = (wifi_speed / 8)
total_time = (file_size / (download_speed / 1024)) / time_factor
print("The total time it will take for your file to download is: " + str(round(total_time, 2)) + " " + str(time))
t.sleep(10)

# [END OF CODE.]

raise SystemExit


