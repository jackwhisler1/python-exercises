from re import sub
from functools import reduce
from operator import mul


def partition(nums, isEven):
    evens, odds = []
    for num in nums:
        if isEven(num):
            evens.append(num)
        else:
            odds.append(num)
    return [evens, odds]


def contains_purple(*args):
    return args.__contains__("purple")


def fav_colors(**kwargs):
    print(kwargs)


def combine_words(word, **kwargs):
    if 'prefix' in kwargs:
        return kwargs["prefix"] + word
    elif 'suffix' in kwargs:
        return word + kwargs["suffix"]
    return word


print(combine_words("rig", prefix="big"))
print(combine_words("big", suffix="boy"))
print(combine_words("big"))


def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = f"{kwargs.get('message', 'The result is')} {float(operation_value)}"
    else:
        final = f"{kwargs.get('message', 'The result is')} {int(operation_value)}"
    return final


def decrement_list(nums):
    return list(map(lambda num: num - 1, nums))


def remove_negatives(nums):
    return list(filter(lambda num: num >= 0, nums))


def is_all_strings(vals):
    return all(isinstance(val, str) for val in vals)


is_all_strings(['a', 'b', 'c'])  # True

print(is_all_strings([2, 'a', 'b', 'c']))  # False

is_all_strings(('hello', 'goodbye'))  # Tru


def interleave(word1, word2):
    pairs = zip(word1, word2)
    # for pair in pairs:
    #     ''.join(pair)
    woven = ''.join([''.join(pair) for pair in pairs])
    print(list(pairs))
    print(woven)


def triple_and_filter(nums):
    multiples_of_four = filter(lambda num: num % 4 == 0, nums)

    return [num * 3 for num in multiples_of_four]


def friend(x):
    return [f for f in x if len(f) == 4]

# Write a function called extract_full_name. This function should accept a list of dictionaries and return a new list of strings with the first and last name keys in each dictionary concatenated.


def extract_full_name(names):
    return [person['first'] + ' ' + person['last'] for person in names]


names = [{'first': 'Elie', 'last': 'Schoppik'},
         {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names))  # ['Elie Schoppik', 'Colt Steele']

# Write a function called divide, which accepts two parameters (you can call them num1 and num2). The function should return the result of num1 divided by num2. If you do not pass the correct type of arguments to the function, it should return the string "Please provide two integers or floats". If you pass as the second argument a 0, Python will raise a ZeroDivisionError, so if this function is invoked with a 0 as the value of num2, return the string "Please do not divide by zero"

# Examples

# divide(4,2)  2
# divide([],"1")  "Please provide two integers or floats"
# divide(1,0)  "Please do not divide by zero"


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Please do not divide by zero"
    except TypeError:
        return "please provide two integers or floats"


# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.


def persistence(n):
    i = 0
    while n >= 10:
        digits = [int(digit) for digit in str(n)]
        n = reduce(mul, digits)
        print(n)
        i += 1
    return i


persistence(11)
persistence(999)

# In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from a to m.

# The colors used by the printer are recorded in a control string. For example a "good" control string would be aaabbbbhaijjjm meaning that the printer used three times color a, four times color b, one time color h then one time color a...

# Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.

# You have to write a function printer_error which given a string will return the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.

# The string has a length greater or equal to one and contains only letters from ato z.

# Examples:
# s="aaabbbbhaijjjm"
# printer_error(s) => "0/14"

# s="aaaxbbbbyyhwawiwjjjwwm"
# printer_error(s) => "8/22"


def printer_error(s):
    errors = sum(1 for l in s if l > 'm')
    print(errors)
    error_count = f'{errors}/{len(s)}'
    print(error_count)
    return error_count


printer_error('asdfasdfmyy')


def printer_error(s):
    return f"{sum(c > 'm' for c in s)}/{len(s)}"


def printer_error(s):
    return "{}/{}".format(len(sub("[a-m]", '', s)), len(s))


def tower_builder(n_floors):
    tower = []
    stars = 1
    for n in range(0, n_floors):

        tower.append(
            f"{' ' * ((n_floors - 1) - n)}{('*' * stars)}{' ' * ((n_floors - 1) - n)}")
        stars += 2
    return tower


print(tower_builder(3))
# # n = 1
# ["  *  "]  # two spaces before/after (len - 1 - i)
# [" *** "]  # one space before/after
# ["*****"]
