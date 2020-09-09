def reverseWords(s):
    words = s.split()
    words_reversed = []

    for word in words:
        words_reversed.append(word[::-1])

    return " ".join(words_reversed)

print(reverseWords("Let's take LeetCode contest"))



#the same as above, just in one line
def reverseWords(s):
    return " ".join([word[::-1] for word in s.split()])


def reverseWords(s):
    if len(s) == 0:
        return s

    s = s.split()

    start = 0
    end = len(s) - 1

    while(start <= end):

        s[start], s[end] = s[end], s[start]

        start += 1
        end -= 1

    return " ".join(s)

"""
Time Complexity: O(n)
"""
