"""
Take input for the montha nd day and idnetify the season it falls within.
"""
month = str(input("What month is it?: "))
month = month.capitalize()

day = int(input("What day is it?: "))


def dayValidation(month, day):
#__This functiion is meant to help eliminate the possibility of the program accepting the input for
 #the day which is higher than the actual number of days in the month__
    if month in ["April", "June", "September", "November"] and day > 30:
            print("!!! There are only 30 days in ", month)
            
    elif month in ["January", "March", "May", "July", "August", "October", "December"] and day > 31:
            print("!!! There are only 31 days in ", month)
            
    elif month == "February" and day > 28:
            print("!!! There are only 28 days in ", month)

    return


if (month == "January" and day <= 31) or (month == "February" and day <= 28) or (month == "March" and day < 20) or (month == "December" and day >= 21):
    dayValidation(month, day)
    print("Winter")

elif (month == "March" and day >= 20) or (month == "April" and day <= 30) or (month == "May" and day <= 31) or (month == "June" and day < 21):
    dayValidation(month, day)
    print("Spring")
    
elif (month == "June" and day >= 21) or (month == "July" and day <= 31) or (month == "August" and day <= 31) or (month == "September" and day < 23):
    dayValidation(month, day)
    print("Summer")

elif (month == "September" and day >= 23) or (month == "October" and day <= 31) or (month == "November" and day <= 30) or (month == "December" and day < 21):
    dayValidation(month, day)
    print("Fall")

else:
    print("!!! You might have inputted wrong month or day")

