def solution(S, C):
    """

    :param S: takes a string of the same many letters eg. 'aabbccc'
    :param C: add price/point to each letter
    :return: removes the highest price from the duplicates and returns sum of the lowest price of letters.
    """
    many = []
    cost = 0
    previous = None
    # We can use "C.append" and "S +=" to force loop to finish last iteration
    # C.append(None)
    # S += '.'
    x = zip(S, C)
    for s, c in x:
        if s != previous:
            previous = s
            if len(many) != 0:
                cost += sum(many) - max(many)
            many = [c]
        else:
            many.append(c)
    # Or we can simply use if statement
    if len(many) != 0:
        cost += sum(many) - max(many)
    return cost

print(solution('aabbccc', [1,2,3,4,5,6,7]))