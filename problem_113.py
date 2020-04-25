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

phrase = "hello world here"

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