def strStr(haystack, needle):

    if len(needle) == 0:
        return 0
    
    if len(haystack) = 0:
        return -1

    if haystack.find(needle) != -1:
        return haystack.index(needle)
    else:
        return -1
