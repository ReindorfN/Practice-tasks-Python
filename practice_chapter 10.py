
#function definitions
#Exercise 10.1
#A function that takes a nested list and returns the sum
def nested_sum(nested_lists) -> list:
    sum = 0
    for index, lists in enumerate(nested_lists):
        for items in range(len(lists)):
            sum += lists[items]
    return sum

#Test
obj1 = nested_sum([[1,2],[3],[4,5,6]])
print(obj1)

#############################################
#Exercise 10.2
def cumsum(list1)-> list:
    new_list = []
    sum = 0
    for index, items in enumerate(list1):
        sum += items
        new_list.append(sum)
    return new_list
 
 #Test
obj2 = cumsum([1,2,3])
print(obj2)

############################################
#Exercise 10.3
def middle(list2) -> list:
    new_list = list2[1:-1]
    return new_list

#Test
obj3 = middle([1,2,3,4])
print(obj3)

###########################################
#Exercise 10.4
def chop(list3) -> list:
    list3 = list3.pop(0) and list3.pop(-1)
    return None

#Test
t = [1,2,3,4,5,6]
chop(t)
print(t)

###########################################
#Exercise 10.5
