def reverseWords(s):
    words = s.split()
    words_reversed = []

    for word in words:
        words_reversed.append(word[::-1])

    return " ".join(words_reversed)

print(reverseWords("Let's take LeetCode contest"))



#the same as above, just in one line
def reverseWords_student_soln(s):
    return " ".join([word[::-1] for word in s.split()])