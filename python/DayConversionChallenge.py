# Write a program to take the number of days as input and convert and display it in
# years, months, weeks and days. (e.g. 452 days equals 1 year, 2 months, 3 weeks and
# 6 days).

# Assume 365 days in a year and 30 days in a month. 
# Link to Twitter post: https://twitter.com/PrasoonPratham/status/1437720304629870592


# Class practice/revision
class ConvertDaysToFormat: 
    def __init__(self, days):
        self.days = days

    def calculation(self): 
        self.Years = (self.days)/365 # Convert days to years
        self.Years = round(self.Years,6)

        self.Months = (self.days)/30 # Convert days to months
        self.Months = round(self.Months,3)

        self.Weeks = (self.days)/7 # Convert days to weeks (30/7 assumes no. of weeks)
        self.Weeks = round(self.Weeks,3)
        self.Days = (self.days) 

    def displayResults(self):
        print("\nThe number of years is: {0}\nThe number months is: {1}\nThe number of weeks is: {2}\nThe number of days is: {3}".format(self.Years,self.Months,self.Weeks,self.Days))

while True:
    try:
        days = int(input("Please enter the amount of days: "))
        break
    except ValueError:
        print("Error, must be an integer value.")

call = ConvertDaysToFormat(days)

call.calculation() # Call functions
call.displayResults()