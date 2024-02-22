

#First section of the task
def alternate_case(string):
    new_string = ''  # initialize an empty string variable to store the new string
    for i, char in enumerate(string):  # iterate through each character in the input string, keeping track of the index
        if i % 2 == 0:  # check if the index is even
            new_string += char.upper()  # if it's even, convert the character to uppercase and add it to the new string
        else:
            new_string += char.lower()  # if it's odd, convert the character to lowercase and add it to the new string
    return new_string  # return the new string with alternate uppercase and lowercase characters

input_string = 'Hello World'
output_string = alternate_case(input_string)
print(output_string)  # Output: 'HeLlO WoRlD'


#Second section of the task
def alternate_words(string):
    words = string.split()  # split the input string into a list of words
    new_words = []
    for i, word in enumerate(words):
        if i % 2 == 0:
            new_words.append(word.lower())
        else:
            new_words.append(word.upper())
    new_string = ' '.join(new_words)  # join the new list of words into a single string
    return new_string

input_string = 'I am learning to code'
output_string = alternate_words(input_string)
print(output_string)  # Output: 'i AM learning TO code'