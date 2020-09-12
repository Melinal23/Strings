"""
The Power Set of a string, consists of all unique combinations of substrings that can be generated from
that original string.

Given a string of characters as your input, write a method that returns the power set of that string, sorted
in lexicographical order.

The output should be given as a list of strings.
"""

def power_set(inputStr):

    sets = []
    mask = 1  # initalize a bit mask

    num_of_sets = pow(2,len(inputStr))

    for i in range(num_of_sets):
        set = ""  # reset sub-set
        count = 0 # reset count
        temp = i 

        while(count < len(inputStr)):
            if (temp >> count) & mask == 1: # if bit at index i is set add char at that index to sub-set
                set += inputStr[count]
            count += 1

        sets.append(set) # append sub-set to list of sets

    return sorted(sets)
    
"""
Time Complexity: O(n * m) where n is num_of_sets and m is length of input string
Space Complexity: O(n) from sets
"""
