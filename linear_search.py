# linear search
from important import fruits


search = input(str("Fruit to search: "))

for c in fruits:
    if search == c:
        print("Fruit is ", fruits.index(c) + 1, "on list.")

if search not in fruits:
    print("Fruit not available")
