"""Problem #2: Run Length Encoding
Practice all aspects of the UMPIRE technique end-to-end and implement a solution for this problem.

Given an input string, write a function that returns the run-length encoded string for the input string.

For example:

Input: "wwwwaaadexxxxxx"
Output: 'w4a3d1e1x6'"""

def run_length_encoding(string):

    if len(string) == 0:
        return string

    dict = {}

    for char in string:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] +=1

    output = ""

    for key in dict:

        output += key + str(dict[key])

    return output

def encode(s):

    encoding = ""  # stores output String

    i = 0
    while i < len(s):
    # count occurrences of character at index i
        count = 1

        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1

        # append current character and its count to the result
        encoding += s[i] + str(count)
        i += 1

    return encoding


print(run_length_encoding("ABCD"))