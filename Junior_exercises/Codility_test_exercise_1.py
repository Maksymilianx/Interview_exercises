def solution(A):
    """
    :param A: an undefined list of 0 and 1
    :return: catches how many 0 should equal 1 or 1 should equal 0 to sort list in [0,1,0,1] or [1,0,1,0,1,0] order.
    """
    x = 0
    k = 0
    for i in A:
        if i != k:
            x += 1
        if k == 0:
            k = 1
        else:
            k = 0
    y = 0
    k = 1
    for i in A:
        if i != k:
            y += 1
        if k == 0:
            k = 1
        else:
            k = 0
    return min(x, y)