def reverse_word_order(string):
    words = string.split()[::-1]

    return " ".join(words)



print(reverse_word_order("The weather is amazing today!"))


def reverse_a_string(string):

    reversed_string = ""   # could make this an array and the join when returning

    for i in range(len(string)-1, -1, -1):
        reversed_string += string[i]

    return reversed_string


print(reverse_a_string("hello"))


def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

#recursion
def reverse2(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

def reverse3(string):
    return "".join(reversed(string))



