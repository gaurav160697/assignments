#1.Write a program to find all pairs of an integer array whose sum is equal to a given number?

def find_pairs(arr, target):
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    return pairs
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10
pairs = find_pairs(arr, target)
print(pairs)  


#2.Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
arr = [1, 2, 3, 4, 5]
reverse_array(arr)
print(arr) 


#3.Write a program to check if two strings are a rotation of each other?

def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    concat = s1 + s1
    if s2 in concat:
        return True
    else:
        return False
s1 = 'gaurav'
s2 = 'ravuag'
if is_rotation(s1, s2):
    print('s2 is a rotation of s1')
else:
    print('s2 is not a rotation of s1')
    
    
#4.Write a program to print the first non-repeated character from a string?

def first_non_repeated_char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None
s = 'abbcdefgghijklmnnop'
result = first_non_repeated_char(s)
if result is not None:
    print('The first non-repeated character in the string is:', result)
else:
    print('There are no non-repeated characters in the string.')
    
    
#5.Read about the Tower of Hanoi algorithm. Write a program to implement it.

def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print('Move disk 1 from', from_rod, 'to', to_rod)
        return
    tower_of_hanoi(n-1, from_rod, aux_rod, to_rod)
    print('Move disk', n, 'from', from_rod, 'to', to_rod)
    tower_of_hanoi(n-1, aux_rod, to_rod, from_rod)
n = 3
tower_of_hanoi(n, 'A', 'C', 'B')


#6.Read about the Tower of Hanoi algorithm. Write a program to implement it.

def postfix_to_prefix(postfix):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    for char in postfix:
        if char not in operators:
            stack.append(char)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(char + op2 + op1)
    return stack.pop()
postfix = '34+5*'
prefix = postfix_to_prefix(postfix)
print('The prefix expression is:', prefix)


#7.Write a program to convert prefix expression to infix expression.


def prefix_to_infix(prefix):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    for char in reversed(prefix):
        if char not in operators:
            stack.append(char)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append('(' + op1 + char + op2 + ')')
    return stack.pop()
prefix = '*+345'
infix = prefix_to_infix(prefix)
print('The infix expression is:', infix)


#8.Read about the Tower of Hanoi algorithm. Write a program to implement it.

def check_brackets(code):
    stack = []
    opening_brackets = set(['(', '[', '{', '('])
    closing_brackets = set([')', ']', '}', ')'])
    bracket_map = {')': '(', ']': '[', '}': '{'}
    for char in code:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or bracket_map[char] != stack.pop():
                return False
    return not stack
code = '(a + b) * [c - {d + e}]'
if check_brackets(code):
    print('All brackets are closed in the code snippet')
else:
    print('Not all brackets are closed in the code snippet')
    
    
#9.Write a program to reverse a stack.

def reverse_stack(stack):
    aux_stack = []
    while stack:
        aux_stack.append(stack.pop())
    while aux_stack:
        stack.append(aux_stack.pop())
stack = [1, 'gaurav', 2, 'karan', 5]
print('Original stack:', stack)
reverse_stack(stack)
print('Reversed stack:', stack)


#10.Write a program to find the smallest number using a stack.

class Stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
    
    def pop(self):
        if not self.stack:
            return None
        value = self.stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value
    
    def get_min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]
stack = Stack()
stack.push(62)
stack.push(54)
stack.push(72)
stack.push(26)
stack.push(87)
print('Smallest number in the stack:', stack.get_min())
