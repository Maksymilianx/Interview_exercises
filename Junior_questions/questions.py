# 1. Difference between Python Arrays and lists

""" Arrays and lists, in Python, have the same way of storing data, however arrays can hold only a single data type
    elements whereas lists can hold any data type elements."""

# Example:

import array as arr

My_array = arr.array('i', [1, 2, 3, 4])
My_lst = [1, 'abc', 1.20]
print(My_array)
print(My_lst)

# 2. What is Lambda function?

""" Lambda function can have any number of parameters but, can have just one statement.
    We use lambda only when we do not want to use this function again."""

a = lambda x, y: x + y
print(a(5, 6))

# 3. What is the difference between sort() and sorted()?

""" sorted() is a function on which we put list as parameter. This function returns new, sorted list """

a = [1, 65, 4, 1, 5, 2, 1, 561, 32]
b = sorted(a)
print(b)

""" sort() is a static list method, which means this function does not return anything but it sorts list on which it 
    is called. """

x = [5, 1, 6, 9, 3, 4, 7, 13]
x.sort()
print(x)

# 4. Generators - When and why do you use them in Python?

""" A generator in Python is a function that returns an iterable object. 
    To retrieve successive elements from the iterator, when writing a generator, we will use the yield statement. 
    We can retrieve a value only once, because generator elements are not stored in memory, 
    and they get their values "on the run".
    
    Generators give us possibility to pause execution of a function or next step as long as we want to keep it.
    For example, if we are operating on large data sets, it is better to use a generator instead of a loop.
    Generators are useful when we don't want all the results right away and we want to pause for a while.
"""


def powers_of_two():
    a = 1
    while True:
        yield (2 ** a)
        a += 1


for i in powers_of_two():
    print(i)
    if i == 2048:
        break

# 5. What's the difference between list and tuple?

"""
    List: is mutable (can be changed), is slower than tuple, can not be key in dict, is restricted by square brackets.
    Tuple: is unmutable (can only be read), is faster than list, can be key in dict, is restricted by round brackets, must have at least one comma.
"""

# 6. What are *args and **kwargs?

"""
    *args are any number of positional parameters in the function. Stored as a tuple.
"""


def add_numbers(*args):
    result = 0
    for num in args:
        result += num
    return result


"""
    **kwargs are any number of dictionary parameters. Stored as a dictionary.
"""


def my_func(**kwargs):
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")


# 7. What are comprehensions?

"""
    Comprehensions are simplified, one-line ways to create a list, dictionary, or generator.
"""

result = []
for i in range(10):
    result.append(2 ** i)

result = [2 ** i for i in range(10)]

# 8. What is decorator and how it's work?

"""
    A decorator is, in short: a function that takes another function as a parameter, 
    modifies its operation, and returns the result.
"""









