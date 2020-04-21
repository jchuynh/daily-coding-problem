# Asked by Microsoft

""" Given a number in the form of a list of digits, return all possible 
permutations.

    >>> permutation([1,2,3])
    [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

"""

# pseudocode:
# first permutation: given
# second: move index 3 to index 2 position
# third: move index 2 to the first position
# continue.. list slicing? stagger the items in the list


# use permutations in itertools?


lst = [1,2,3]

def permutations(lst):
    """ Given a number in the form of a list of digits, return all possible
    permutations."""

    new_lst = []

    for i in range(len(lst)):
        m = lst[i]

        remaining_lst = lst[:i] + lst[i+1:]

        for per in premutations(remaining_lst):
            new_lst.append([m] + p)
    return new_lst

permutations(lst)





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** Test Pass! \n")
