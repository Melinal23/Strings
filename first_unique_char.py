from collections import OrderedDict

def firstUniqChar(s):
    d = OrderedDict()

    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = [i, 1]
        else:
            d[s[i]][1] += 1

    for item in d.values():
        if item[1] == 1:
            return item[0]

    return -1