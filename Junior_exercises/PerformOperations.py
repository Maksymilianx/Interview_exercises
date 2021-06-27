def performOperations(arr, operations):
    """

    :param arr: a list of integers
    :param operations: integers in list to be reversed
    :return: a list with reversed operations integers
    """
    for operation in operations:
        submatrix = arr[operation[0]:operation[1] + 1]
        submatrix = submatrix[::-1]
        arr[operation[0]:operation[1] + 1] = submatrix
    return arr

print(performOperations([1,3,4,1,6,2],[[2,3]]))