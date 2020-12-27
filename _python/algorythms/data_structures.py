import sys


def is_balanced(s):
    stack = []
    for char in s:
        if char in '[(':
            stack.append(char)
        elif char in '])':
            if len(stack) != 0:
                top = stack.pop()
                if (top == '('and char != ')') or (top == '['and char != ']'):
                    return False
            elif stack == []:
                return False
    if stack == []:
        return True


print(is_balanced('()[]([])(())'))


def min_of_3(l, m):
    for i in range(len(l)):
        if len(l[i:m+i]) > 2:
            print(l[i:m+i], sum(l[i:m+i]))


min_of_3([5, 1, 3, 2, 4, 6, 1, 7, 3, 2, 8], 3)
# x = input(':')
# print(x)
print(sys.version)
