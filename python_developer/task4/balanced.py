def is_balanced(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in "({[":
            stack.append(char)  
        elif char in ")}]":
            if not stack or stack.pop() != pairs[char]:
                return False  

    return not stack  
print(is_balanced("(){}[]"))
print(is_balanced("{[()]}"))  
print(is_balanced("{[(])}"))  
print(is_balanced("({}["))    
