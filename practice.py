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
