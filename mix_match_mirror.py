"""
Given a string of only lowercase alphabetical characters, determine whether there is some arrangement
of those characters that creates a word that is the same forwards and backwards

We can consider any rearrangement of the characters. For example, valid arrangements of abc are
bca, acb, bac, cab, and cba.

A mirrored word is any word that reads the same forwards, and backward. For example, mom, racecar, abba.

Your objective is to determine if a given set of characters can be rearranged to read the same forwards
and backward.
"""

def mix_match_mirror(word):

    temp = []
    perms = []

    for char in word:
        temp.append(char)

    permutations(temp, 0, len(temp)-1, perms) # find permutations

    return is_palindrome(perms)  # determine if any are mirrored


# this function find all the possible arrangement of characters from the given word
def permutations(word, start, end, perms):

    if start == end:
        perms.append("".join(word))
    else:
        for i in range(start, end+1):
            word[start], word[i] = word[i], word[start]  # swap
            permutations(word, start + 1, end, perms)  # recursively call with the rest of word
            word[start], word[i] = word[i], word[start]  # backtrack



# this function determine if any of the given arrangements are palindromes
def is_palindrome(perms):
    for word in perms:
        if determine_pal(word):
            return True

    return False

def determine_pal(word):

    start = 0
    end = len(word) - 1

    while(start <= end):

        if word[start] != word[end]:
            return False

        start += 1
        end -= 1

    return True
