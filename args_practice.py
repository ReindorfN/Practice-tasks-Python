
def calculate_average_1(some_list):
    sum_of_list = sum(some_list)
    number_of_items = len(some_list)
    return sum_of_list / number_of_items

example_list = [2,3,4,5]
result = calculate_average_1(example_list)
print(result)


def calculate_average_2(*args):
    sum_of_list = sum(args)
    number_of_items = len(args)
    return sum_of_list / number_of_items

result = calculate_average_2(2,3,4,5,6)
print(result)

def concatenate_strings(*args):
    joined_strings = "---".join(args)
    print(joined_strings)

result = concatenate_strings("Hello", "World", "My", "Tawiah")
print(result)