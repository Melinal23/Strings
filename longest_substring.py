"""A sliding window is an abstract concept commonly used in array/string problems. A window is a range
of elements in the array/string which usually defined by the start and end indices, i.e. [i, j)[i,j) (left-closed,
right-open). A sliding window is a window "slides" its two boundaries to the certain direction. For example,
if we slide [i, j)[i,j) to the right by 11 element, then it becomes [i+1, j+1)[i+1,j+1) (left-closed, right-open)."""


def lengthOfLongestSubstring(s):
    string_size = len(s)
    seen = set()
    length = i = j = 0

    while (i < string_size and j < string_size):
        if s[j] not in seen:
            seen.add(s[j])
            j += 1
            length = max(length, j - i)
        else:
            seen.remove(s[i])
            i += 1

    return length

# print(lengthOfLongestSubstring("abcdefg"))


#Given a string, find the length of the longest substring in it with no more than K distinct characters

def lengthOfLongestSubstringWithKDistinct(s, k):
    string_size = len(s)
    seen = set()
    length = i = j = 0

    while (i < string_size and j < string_size):
        if s[j] not in seen and len(seen) <= k:
            seen.add(s[j])
            j += 1
            length = max(length, j - i)
        else:
            if len(seen) >= k:
                seen.remove(s[i])
                i += 1
            elif s[j] in seen:
                j +=1
                length = max(length, j - i)

    return length

# print(lengthOfLongestSubstringWithKDistinct("aaaaaj",3))
# print(lengthOfLongestSubstringWithKDistinct("araaci",1))
print(lengthOfLongestSubstringWithKDistinct("cbbebi",3))