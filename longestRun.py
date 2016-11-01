def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """

    # prevNumber = 0
    # currentList = []
    # longestList = []
  
    # for number in L:
    #     if prevNumber <= number:
    #         currentList.append(number)
    #     elif number >= prevNumber:
    #         currentList.append(number)
    #     else: 
    #         if len(currentList) > len(longestList):
    #             longestList = currentList
    #     prevNumber = number

    # if len(currentList) > len(longestList):
    #     longestList = currentList
    
    # return sum(longestList)
    # print(longestList, sum(longestList))

    current_increasing = []
    longest_increasing = []
    current_decreasing = []
    longest_decreasing = []

    listCopy = L[1:]
    listCopy.append(L[-1])
    
    for x, y in zip(L,  listCopy):
        print(L, listCopy, x, y)
        if x <= y:
            current_increasing.append(x)
            print('increase', current_increasing)
            longest_increasing = current_increasing
            
            # print(longest_increasing)

        if x >= y:
            # print('decrease')
            current_decreasing.append(x)
            print('decrease', current_decreasing, x, y)
            longest_decreasing = current_decreasing
            # print(longest_decreasing)
    print('longest check', longest_increasing, longest_decreasing)
    winning_list = max(longest_increasing, longest_decreasing)
    print('end', winning_list, sum(winning_list))
    # return winning_list

# longest_run([1, 2, 3, 4, 5, 6, 7, 8, 9])
# longest_run([1, 2, 3, 2, 1])
# longest_run([3, 2, 1, 2, 3])
# longest_run([1, 2, 1, 2, 1, 2, 1, 2, 1])
# longest_run([1, 2, 3, 4, 5, 0, 10, 1, 2, 3, 4, 5])
# longest_run([1, 2, 3, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
# longest_run([1, 2, 3, 2, -1])
# longest_run([3, 2, -1, 2, 7])
# longest_run([100, 200, 300, -100, -200, -1500, -5000])
# longest_run([100, 200, 300, 400, 0, 10000, 20000])
longest_run([1, 2, 3, 2, -1, -10])
# longest_run([3, 3, 3, 3, 3, 3, 3, -10, 1, 2, 3, 4])
# longest_run([3, 4, 5, 6, 10, 20, 100, 200, 1, 3, 3, 3, -10, 1, 2, 3, 4])
# longest_run([3, 3, 3, 3, 3])
# longest_run([-3, -3, -3, -3, -3])


# def longest_run(L):
#     """
#     Assumes L is a list of integers containing at least 2 elements.
#     Finds the longest run of numbers in L, where the longest run can
#     either be monotonically increasing or monotonically decreasing. 
#     In case of a tie for the longest run, choose the longest run 
#     that occurs first.
#     Does not modify the list.
#     Returns the sum of the longest run. 
#     """
#     current_increasing = []
#     longest_increasing = []
#     current_decreasing = []
#     longest_decreasing = []

#     listCopy = L[1:]
#     listCopy.append(L[-1])

#     for x, y in zip(L,  listCopy):
#         if x <= y:
#             current_increasing.append(x)
#             longest_increasing = current_increasing

#         if x >= y:
#             current_decreasing.append(x)
#             longest_decreasing = current_decreasing

#     winning_list = max(longest_increasing, longest_decreasing)
#     return winning_list