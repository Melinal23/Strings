def isAnagram(s, t):

    if len(s) != len(t):
        return False

    dict1 = {}
    dict2 = {}

    for char in s:
        if char in dict1:
            dict1[char] += 1
        else:
            dict1[char] = 1

    for char in t:
        if char in dict2:
            dict2[char] += 1
        else:
            dict2[char] = 1

    for item in dict1:
        if item not in dict2:
            return False
        else:
            if dict1[item] != dict2[item]:
                return False
    return True


def isAnagram_leetsoln(s, t):

    if len(s) != len(t):
        return False

    counter = [0] * 26

    for i in range(len(s)):
        counter[ord(s[i]) - ord('a')] += 1
        counter[ord(t[i]) - ord('a')] -= 1

    for item in counter:
        if item != 0:
            return False

    return True


def isAnagram_studentsoln(s,t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)