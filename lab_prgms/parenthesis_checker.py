def check_balanced_parentheses(expression):
    stack = []
    opening_parentheses = {'(', '{', '['}
    closing_parentheses = {')', '}', ']'}
    matching_pair = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in expression:
        if char in opening_parentheses:
            stack.append(char)
        elif char in closing_parentheses:
            if not stack:  
                return False
            
            top_char = stack.pop()
            
            if top_char != matching_pair[char]:
                return False
        
    return not stack

if __name__ == "__main__":
    test_expressions = [
        "({[a+b]*(c-d)})",      # Balanced
        "((()))",               # Balanced
        "[{()}]",               # Balanced
        "([{}])",               # Balanced
        "({[)}",                # Unbalanced (wrong match)
        "((()))(",              # Unbalanced (unclosed opening)
        ")(()",                 # Unbalanced (closing without opening)
        "abc",                  # No parentheses, considered balanced
        "",                     # Empty string, considered balanced
        "([)]",                 # Unbalanced (wrong order)
        "{[()]}"                # Balanced
    ]

    for expr in test_expressions:
        result = check_balanced_parentheses(expr)
        print(f"Expression: '{expr}' -> Balanced: {result}")