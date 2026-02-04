def isBalanced(string):
    stack = []

    map ={
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }

    for char in string:

        if char in map.values():
            stack.append(char)

        elif char in map :
            '''If stack is empty or mismatch between top of stack return false'''
            if  not stack or stack[-1] != map[char]:
                return False
            stack.pop()

    return len(stack) == 0

print(isBalanced("(()[]{})"))



