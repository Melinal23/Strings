def valid_braces(braces):

    b = {']' : '[', '}': '{', ')': '(' }

    stack = []

    for brace in braces:
        if brace in b:
            if len(stack) == 0:
                return False
            if stack.pop() != b[brace]:
                return False
        else:
            stack.append(brace)

    return True


print(valid_braces("{{}[]}"))