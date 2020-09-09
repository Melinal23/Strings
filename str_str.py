def strStr(haystack, needle):

    if len(needle) == 0:
        return 0
    
    if len(haystack) = 0:
        return -1

    if haystack.find(needle) != -1:
        return haystack.index(needle)
    else:
        return -1

 # without built-in functions
def strStr(haystack, needle):

    if len(needle) == 0:
        return 0

    if len(haystack) == 0 or len(needle) > len(haystack):
        return -1

    for i in range(len(haystack)):
        for j in range(len(needle)):
            if i + j == len(haystack):
                return -1
            if needle[j] != haystack[i+j]:
                break 
            if j == len(needle)-1: 
                return i

    return -1
        
