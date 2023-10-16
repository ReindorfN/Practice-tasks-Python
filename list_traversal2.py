
#Initializers
numbers = [2,3,5,4,67,54,32,19]
numbers_new = []
other_numbers = [12, 64,43,18,0]
numbers.extend(other_numbers)

# Function definitions
def item_multiply():
    for i in range(len(numbers)):
        numbers_new.append(numbers[i] *2)
    return numbers, numbers_new

def item_sort(): #This is unneccessary.
    sub = 0
    for i in range(len(numbers)):
        if numbers[i] > numbers[i+1]:
            sub = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = sub

def add_all():
    total = 0
    for x in numbers:
        total += x
    return total
            
#print outs
obj1 = item_multiply()
print(obj1)
print()

obj2 = add_all()
print(numbers)
print(obj2)
print()

numbers.sort()
print(numbers)
