# 1.Implement Binary Tree
class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
   def PrintTree(self):
      print(self.data)

root = Node(10)
root.PrintTree()

# 2.Find height of a given tree

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def height(node):
    if node is None:
        return 0

    left_height = height(node.left)
    right_height = height(node.right)

    return max(left_height, right_height) + 1
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(height(root))  

# 3.Perform Pre-order, Post-order, In-order traversal

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def pre_order_traversal(node):
    if node:
        print(node.value)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.value)
        in_order_traversal(node.right)

def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.value)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Pre-order traversal:")
pre_order_traversal(root)

print("In-order traversal:")
in_order_traversal(root)

print("Post-order traversal:")
post_order_traversal(root)

# 4.Function to print all the leaves in a given binary tree

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def print_leaves(node):
    if node is None:
        return

    if node.left is None and node.right is None:
        print(node.value)

    print_leaves(node.left)
    print_leaves(node.right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.left = Node(8)

print_leaves(root)  


# 5.Implement BFS (Breath First Search) and DFS (Depth First Search)

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs(root):
    if root is None:
        return []

    visited = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        visited.append(node.value)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return visited
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(bfs(root))

# 6.Find sum of all left leaves in a given Binary Tree

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def sum_left_leaves(node, is_left=False):
    if node is None:
        return 0

    if node.left is None and node.right is None:
        if is_left:
            return node.value
        else:
            return 0

    return sum_left_leaves(node.left, True) + sum_left_leaves(node.right, False)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.left = Node(8)

print(sum_left_leaves(root)) 

# 7.Find sum of all nodes of the given perfect binary tree

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def perfect_tree_sum(root):
    if root is None:
        return 0

    height = 0
    node = root
    while node.left is not None:
        height += 1
        node = node.left

    return (2**(height+1)) - 1
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(perfect_tree_sum(root))

# 8.Count subtress that sum up to a given value x in a binary tree

class getNode:
    def __init__(self, data):
 
        self.data = data
        self.left = self.right = None
 
def countSubtreesWithSumX(root, count, x):
 
    if (not root):
        return 0
    ls = countSubtreesWithSumX(root.left,
                               count, x)
 
    rs = countSubtreesWithSumX(root.right,
                               count, x)
 
    
    Sum = ls + rs + root.data
 
    if (Sum == x):
        count[0] += 1
 
    return Sum
 
 
def countSubtreesWithSumXUtil(root, x):
 
    if (not root):
        return 0
 
    count = [0]
 
    ls = countSubtreesWithSumX(root.left,
                               count, x)
 
    rs = countSubtreesWithSumX(root.right,
                               count, x)
    if ((ls + rs + root.data) == x):
        count[0] += 1
    return count[0]
if __name__ == '__main__':
    root = getNode(5)
    root.left = getNode(-10)
    root.right = getNode(4)
    root.left.left = getNode(9)
    root.left.right = getNode(12)
    root.right.left = getNode(-6)
    root.right.right = getNode(7)
 
    x = 7
 
    print("Count =",
          countSubtreesWithSumXUtil(root, x))
# 9.Find maximum level sum in Binary Tree

from collections import deque

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def max_level_sum(root):
    if root is None:
        return 0

    max_sum = float('-inf')
    max_level = 0
    level = 0
    queue = deque([root])

    while queue:
        level += 1
        level_sum = 0
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()
            level_sum += node.value

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if level_sum > max_sum:
            max_sum = level_sum
            max_level = level

    return max_level


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

max_sum_level = max_level_sum(root)
print(f"Maximum level sum is at level {max_sum_level}") 
          
# 10.Print the nodes at odd levels of a tree

class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
 
def printOddNodes(root, isOdd = True):
     
    if (root == None):
        return
 
    
    if (isOdd):
        print(root.data, end = " ")
 
    
    printOddNodes(root.left, not isOdd)
    printOddNodes(root.right, not isOdd)

if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    printOddNodes(root)
