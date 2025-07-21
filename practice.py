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
