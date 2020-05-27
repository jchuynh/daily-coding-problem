# asked by Google

# given an array of numbers and an index i, return the index of the 
# nearest largest number of the number at the index i, where the distance is 
# measured in array indices.
# if two distances to larger numbers are equak, the return ant one of them. If
# the array at i doesn't have a nearest larger integer, then return null.

def nearest_larger(arr, I):
    """

    >>>[4, 1, 3, 5, 6]
    3
    """

    # pseudocode
    # run through the list to find the value at I
    for idx, val in enumerate(arr):
    # look through the list to see the nearest larger value
        if idx = I:
            return val
    # return the value's index



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** Test Pass! \n")