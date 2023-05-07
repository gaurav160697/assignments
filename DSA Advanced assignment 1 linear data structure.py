# 1.Delete the elements in an linked list whose sum is equal to zero

class Node():
  def __init__(self,data):
     self.data = data
     self.next = None

class Linkedlist():
   def __init__(self):
     self.head = None
    
   def append(self,data):
     new_node = Node(data)
     h = self.head
     if self.head is None:
         self.head = new_node
         return
     else:
         while h.next!=None:
             h = h.next
         h.next = new_node

   def remove_zeros_from_linkedlist(self, head):
     stack = []
     curr = head
     list = []
     while (curr):
         if curr.data >= 0:
             stack.append(curr)
         else:
             temp = curr
             sum = temp.data
             flag = False
             while (len(stack) != 0):
                 temp2 = stack.pop()
                 sum += temp2.data
                 if sum == 0:
                     flag = True
                     list = []
                     break
                 elif sum > 0:
                     list.append(temp2)
             if not flag:
                 if len(list) > 0:
                     for i in range(len(list)):
                         stack.append(list.pop())
                 stack.append(temp)
         curr = curr.next
     return [i.data for i in stack]

if __name__ == "__main__":
 l = Linkedlist()

 l.append(4)
 l.append(6)
 l.append(-10)
 l.append(8)
 l.append(9)
 l.append(10)
 l.append(-19)
 l.append(10)
 l.append(-18)
 l.append(20)
 l.append(25)
 print(l.remove_zeros_from_linkedlist(l.head))


class Node:
  
    
    def __init__(self, data):
        self.data = data
        self.next = None
  
  
class LinkedList:
  
    def __init__(self):
        self.head = None
  
    def reverse(self, head, k):
        
        if head == None:
          return None
        current = head
        next = None
        prev = None
        count = 0
        while(current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
        if next is not None:
            head.next = self.reverse(next, k)
  
        return prev
  
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end=' ')
            temp = temp.next
llist = LinkedList()
llist.push(74)
llist.push(12)
llist.push(45)
llist.push(25)
llist.push(41)
llist.push(65)
llist.push(37)
llist.push(26)
llist.push(10)
  
print("Given linked list")
llist.printList()
llist.head = llist.reverse(llist.head, 3)
  
print ("\nReversed Linked list")
llist.printList()

# 3.Merge a linked list into another linked list at alternate positions.

class Node(object):
    def __init__(self, data:int):
        self.data = data
        self.next = None
  
  
class LinkedList(object):
    def __init__(self):
        self.head = None
          
    def push(self, new_data:int):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
  
    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next
   
    def merge(self, p, q):
        p_curr = p.head
        q_curr = q.head
  
        while p_curr != None and q_curr != None:
  
            p_next = p_curr.next
            q_next = q_curr.next
  
            q_curr.next = p_next  
            p_curr.next = q_curr  
  
            p_curr = p_next
            q_curr = q_next
            q.head = q_curr
  
llist1 = LinkedList()
llist2 = LinkedList()
  
# 1.
llist1.push(3)
llist1.push(2)
llist1.push(1)
llist1.push(0)
  
# 2.
for i in range(8, 3, -1):
    llist2.push(i)
  
print("First Linked List:")
llist1.printList()
  
print("Second Linked List:")
llist2.printList()
  
llist1.merge(p=llist1, q=llist2)
  
print("Modified first linked list:")
llist1.printList()
  
print("Modified second linked list:")
llist2.printList()


# 4.In an array, Count Pairs with given sum

def getPairsCount(arr, n, sum):
 
    count = 0  
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count += 1
 
    return count

arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
print("Count of pairs is",
      getPairsCount(arr, n, sum))


# 5.Find duplicates in an array

numRay = [0, 4, 3, 2, 7, 8, 2, 3, 1]
arr_size = len(numRay)
for i in range(arr_size):
  
    x = numRay[i] % arr_size
    numRay[x] = numRay[x] + arr_size
  
print("The repeating elements are : ")
for i in range(arr_size):
    if (numRay[i] >= arr_size*2):
        print(i, " ")
        
        
# 6.Find the Kth largest and Kth smallest number in an array

from typing import List




class Solution:
    def kth_Largest_And_Smallest_By_AscendingOrder(self, arr: List[int], k: int) -> None:
        arr.sort()
        n = len(arr)


        print(
            f"kth Largest element {arr[n - k]}, kth Smallest element {arr[k - 1]}")




if __name__ == "__main__":
    arr = [1, 2, 6, 4, 5, 3]
    Solution().kth_Largest_And_Smallest_By_AscendingOrder(arr, 3)
    
# 7. Move all the negative elements to one side of the array


def rearrange(arr, n ) :

    j = 0
    for i in range(0, n) :
        if (arr[i] < 0) :
            temp = arr[i]
            arr[i] = arr[j]
            arr[j]= temp
            j = j + 1
    print(arr)

arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
n = len(arr)
rearrange(arr, n)


# 8.Reverse a string using a stack data structure

def createStack():
    stack = []
    return stack

def size(stack):
    return len(stack)

def isEmpty(stack):
    if size(stack) == 0:
        return true
def push(stack, item):
    stack.append(item)
def pop(stack):
    if isEmpty(stack):
        return
    return stack.pop()
def reverse(string):
    n = len(string)
    stack = createStack()
    for i in range(0, n, 1):
        push(stack, string[i])
    string = ""
    for i in range(0, n, 1):
        string += pop(stack)
    return string
string = "GauravDhote"
string = reverse(string)
print("Reversed string is " + string)


# 9.Evaluate a postfix expression using stack

class Evaluate:
 
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.array = []
 
    def isEmpty(self):
        return True if self.top == -1 else False
 
    def peek(self):
        return self.array[-1]
 
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
    def push(self, op):
        self.top += 1
        self.array.append(op)
 
    def evaluatePostfix(self, exp):
 
        for i in exp:
 
            if i.isdigit():
                self.push(i)
 
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push(str(eval(val2 + i + val1)))
 
        return int(self.pop())
 
if __name__ == '__main__':
    exp = "231*+9-"
    obj = Evaluate(len(exp))
    print("postfix evaluation: %d" % (obj.evaluatePostfix(exp)))
    
    
# 10.Implement a queue using the stack data structure

class Queue: 
    def __init__(self):
        self.s1 = []
        self.s2 = []
  
    def enQueue(self, x):
          
        
        while len(self.s1) != 0: 
            self.s2.append(self.s1[-1]) 
            self.s1.pop()
  
       
        self.s1.append(x) 
  
        
        while len(self.s2) != 0: 
            self.s1.append(self.s2[-1]) 
            self.s2.pop()
  
    
    def deQueue(self):
          
            
        if len(self.s1) == 0: 
            print("Q is Empty")
      
        
        x = self.s1[-1] 
        self.s1.pop() 
        return x

if __name__ == '__main__':
    q = Queue()
    q.enQueue(1) 
    q.enQueue(2) 
    q.enQueue(3) 
  
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
