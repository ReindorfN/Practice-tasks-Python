# Count of the number of characters in a string

def alpha_count(string):
    my_dict = {}
    list1 = list(string)
    for char in list1:
        if char not in my_dict:
            my_dict[char] = 1
        else:
            my_dict[char] += 1
    my_dict = sorted(my_dict.items())
    for items in my_dict:
       print(items)

print(alpha_count("hello world"))
