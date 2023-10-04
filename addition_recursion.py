#
#Recursion function to add user input until black line is inputed.
#

def total_values():
    user_input = input("Enter the number: ")
    
    if user_input == "":
        return 0.0
    else:
        return float(user_input) + total_values()
    
result = total_values()
print(result)
