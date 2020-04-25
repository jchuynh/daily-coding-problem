# Asked by Google - Medium 

"""
Given a string of words delimited by spaces, reverse the words in string. 
For example, given "hello world here", return "here world hello".

Follow-up: given a mutable string representation, can you perform this 
operation in-place?

test case:
>>> reverse_words("hello world here")
here world

"""

# GENERAL NOTES: 
# reversed() - to return the reverse string
# import re - Python regex module 
# list slicing - [start, stop, step]
phrase = "hello world here"

# reverse_words notes:
# Uses O(n) time complexity
# does not take into account punctuations

def reverse_words(phrase):
    # pseudocode:
    # use spaces to define each word set
    # append each word to a new list
    new_string = " "
    word_lst = phrase.split()
    # use indices to navigate the reverse phrase
    for item in word_lst:
        rev = word_lst[::-1]
    # return should be in str() format
    print(new_string.join(rev))


reverse_words(phrase)


def reverse_words_recursion(phrase):
    if len(phrase) == 0:
        return phrase
    else:
        # Slice the part of the string except the first character and concatenate
        # the first character to the end of the sliced string.
        return reverse(phrase[1:]) + phrase[0]

