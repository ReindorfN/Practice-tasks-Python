
#function that returns the sum of squares of a list.
def sum_of_squares(xs) ->list:
    squares = []
    sum = 0
    for i in xs:
        squares.append(i**2)
        

    for i in squares:
        sum += i
    return sum

obj1 = sum_of_squares([2,4,3])
print(obj1)

