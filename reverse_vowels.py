"""
Given a string as an input, return a copy of that string, except with the order of all of its
vowels reversed. The order of the constants should stay the same.

For example, given the string word = "san francisco", the output would be "son frincasca."

Return a copy of the original string with its vowels reversed.
"""
def reverse_vowels(word):

    vowels = {'a', 'e', 'i', 'o', 'u'}
    temp = []

    for char in word:
        temp.append(char)

    start = 0
    end = len(temp) - 1

    while(start <= end):

        while start <= end and temp[start] not in vowels: # use a running ptr to skip over constants
            start += 1

        while end >= start and temp[end] not in vowels:  # use a running ptr to skip over constants from the end
            end -= 1


        if start <= end and end >= start:  # as long as we are in bounds
            temp[start], temp[end] = temp[end], temp[start]  # swap the vowels
            start += 1
            end -= 1

    return "".join(temp)
