# asked by Snapchat


def rooms_needed(times):
    """
    Given an array of time intervals (start, end) for classroom lectures (possibly    
    overlapping), find the minimum number of rooms required.

    >>> rooms_needed([(30, 75), (0, 50), (60, 150)])
    2
    """

    # Pseudocode (On^2)
    # start a counter of how many room are required.
    rooms = 0
    # sort times
    # srted_times = sorted(times)
    # if the end time is greater than the start time on the next tuple
    for time1 in times:
        for time2 in times:
            if time1[0] > time2[0] and time1[0] < time2[1]:
                rooms += 1

    return rooms




    # for end_time in times[0]:
    #     # for start_time in srted_times[1:]:
    #     if end_time >= start_time:
    #         rooms += 1


    # for time in range(len(srted_times)):
    #     for start in range(time + 1, len(srted_times)):
    #         print(start)
            # if start >= time[1]:
            #     rooms += 1
        # if start >= 
    # add one to the counter
    # continue to loop through the other times. 


    

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS. \n")
