readingfile = open("reading.txt", "r")

firstline = readingfile.readline()
print("the first line of the file is: ", firstline)
secondline = readingfile.readline()
print("the second line of the file is: ", secondline)

"""
all_lines = readingfile.readlines()
print(all_lines)
"""

print(readingfile.read())