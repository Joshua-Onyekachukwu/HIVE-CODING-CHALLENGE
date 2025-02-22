def is_balanced(bracket_string):
    # Define a mapping of closing brackets to their corresponding opening brackets
    bracket_pairs = {')': '(',
                     '}': '{',
                     ']': '['}

    # Initialize an empty stack
    stack = []

    # Iterate through each character in the string
    for char in bracket_string:
        # If the character is an opening bracket, push it onto the stack
        if char in bracket_pairs.values():
            stack.append(char)
        # If the character is a closing bracket
        elif char in bracket_pairs:
            # Check if the stack is empty or the top of the stack doesn't match
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            # Pop the matching opening bracket from the stack
            stack.pop()

    # If the stack is empty, the string is balanced
    return not stack


# Test cases
print(is_balanced("{[()]}"))  # True
print(is_balanced("{[(])}"))  # False
print(is_balanced("{{[[(())]]}}"))  # True
print(is_balanced("({)}"))  # False