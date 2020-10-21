
def first_non_repeating_character1(inputStr):

    dict = {}

    for char in inputStr:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1

    for char in inputStr:
        if dict[char] == 1:
            return char

    return None

"""
Time Complexity: O(n) because of the 2 for loops n + n = 2n ==> n
Space Complexity: O(n) because of the dictionary
"""


# print(first_non_repeating_character1("aaabbbcccddd"))
# print(first_non_repeating_character1("aaaaafbgd"))


def first_non_repeating_character2(inputStr):

    chars = [0] * 26


    for char in inputStr:
        chars[ord(char.lower()) - 97] += 1

    for char in inputStr:
        if chars[ord(char.lower()) - 97] == 1:
            return char

    return None

"""
Time Complexity: O(n) because of the 2 for loops n + n = 2n ==> n
Space Complexity: O(n) because of the array
"""

print(first_non_repeating_character2("aaabbbcccdddj"))
print(first_non_repeating_character1("aaazaahhbfbgd"))