
def first_vowel(s):
    for index, char in enumerate(s):
        if char in 'aeiou':
            return index
    raise Error('No vowel found')


def convert(s):
    index = first_vowel(s)
    return s[index:]  + s[:index] + 'ay'

#print(convert("sleep"))
    

def pig_latin(word):
    if word[0] not in "aeiou":
        new_word = convert(word)
        print(new_word)
    else:
        new_word += "way"
        print(new_word)

pig_latin("predate")
