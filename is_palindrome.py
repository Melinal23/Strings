def isPalindrome(s):

    if s == "":    # an empty string is a palindrome
        return True

    s = "".join([x for x in s if x.isalpha() or x.isdigit()])

    start = 0
    end = len(s) - 1

    while(start <= end):

        if s[start].lower() != s[end].lower():
            return False

        start += 1
        end -= 1

    return True

"""
Time Complexity: O(n)
Space Complexity: O(1)

"""

def isPalindrome(s):

    if s == "":    # an empty string is a palindrome
        return True

    start = 0
    end = len(s) - 1

    while(start <= end):

        while s[start].isalpha() == False and s[start].isdigit() == False and start < end:
            start += 1

        while s[end].isalpha() == False and s[end].isdigit() == False and start < end:
            end -= 1

        if s[start].lower() != s[end].lower():
            return False

        start += 1
        end -= 1

    return True
