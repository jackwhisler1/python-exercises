list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
answer = [num for num in list1 if num in list2]
print(answer)
names = ["Elie", "Tim", "Matt"]
answer2 = [name[-1::-1].lower() for name in names]
print(answer2)

# Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string (alphabetical ascending), the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.


def longest(a1, a2):
    return ''.join(sorted(set(a1 + a2)))


a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
print(longest(a, b))  # -> "abcdefklmopqwxy"
