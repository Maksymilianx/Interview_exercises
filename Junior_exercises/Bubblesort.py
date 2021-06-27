sort_this = [10, 2, 7, 5, 53, 11, 35, 0, 4, 6, 12]

def sort(data):
    """
    Bubble sort
    :param data: a list to be sorted
    :return: a sorted list
    """
    iteration = len(data)
    while iteration > 0:
        for i in range(0, iteration -1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
        iteration -= 1
    return data
