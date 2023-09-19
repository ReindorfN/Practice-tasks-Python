import random
from important import character

number_passwords = int(input("Number of passwords: "))
Lenght_password = int(input("lenght of password: "))

for i in range(number_passwords):
	password = " "
	for c in range(Lenght_password):
		password += random.choice(character)
	print("The password generated is: ", password)
print("Done!!")