import pytest

class Node:
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return str(self.data)

# Could implement without this wrapper
class SinglyLinkedList:

    def __init__(self, head=None):
        self.head = head
        self._size = 0
    
    def append(self, node):
        curr = self.head

        while curr.next != None:
            curr = curr.next

        curr.next = node

        self._size += 1

    def get(self, pos):
        if pos > self._size:
            raise IndexError("Out of range")

        curr = self.head

        for i in range(pos):
            if curr == None:
                raise IndexError("Out of range")
            curr = curr.next

        return curr

    def __repr__(self):
        curr = self.head
        l = []
        while curr.next != None:
            l.append(repr(curr))
            curr = curr.next

        l.append(repr(curr))
        return str(l)
    
    def _find(self, data):
        prev = None
        curr = self.head
        
        while curr.data != data:
            if curr.next == None:
                return (None, None)
            prev = curr
            curr = curr.next

        return (prev, curr)


def weave(l):
    s = l.head
    f = l.head

    if l._size < 3:
        print("Too small!")
        return

    while f.next != None and f.next.next != None:
        s = s.next
        f = f.next.next

        
    # When f hits the end, s wil be at the midpoint
    # Move f back to the front, and weave them together
    # a1 -> a2 -> ... -> an -> b1 -> b2 -> ... -> bn
    #                           ^                  ^
    # a1 -> a2 -> ... -> an -> b1 -> b2 -> ... -> bn
    #  ^                        ^ 

    f = l.head
    s = s.next
    print(f, s)

    while s != None:
        oldfnext = f.next
        f.next = s
        f = oldfnext
        oldsnext = s.next

        if (s.next != None):
            s.next = f;
        s = oldsnext;

    return l
    
"""
2.1 Remove Dups

Write code to remove duplicates from an unsorted linked list.
"""

def remove_dups1(l):
    
    curr = l.head
    while curr != None:
        curr2 = curr
        print(f"Searching for {curr.data}")
        while curr2.next != None:
            if curr.data == curr2.next.data:
                print(f"Found {curr.data}")
                curr2.next = curr2.next.next
            else:
                curr2 = curr2.next
        curr = curr.next

    return l

def kth_last(l, k):
    s = l.head
    f = l.head 
    count = 0
    while f != None:
        f = f.next
        if count >= k:
            s = s.next
        count += 1

    return s

def kth_last2(l, k): 
  index = kth_last2helper(l.head, k) 
  return l.get(index)

def kth_last2helper(node, k):
  # We've hit the end
  if node == None:
      return 0
  
  index = kth_last2helper(node.next, k) + 1
  if index == k:
      print(f"found: {node.data}")
  return index
            
class TestLinkedList:
    def __init__(self):
        self.l = SinglyLinkedList(head=Node(1))

    def test_append(self):
        self.l.append(Node(3))
        self.l.append(Node(19))
        assert self._l.size == 3

    def test_get(self):
        assert self.l.get(2) == 19

if __name__ == "__main__":
    lst = SinglyLinkedList(head=Node(11))
    lst.append(Node(12))
    lst.append(Node(13))
    lst.append(Node(14))
    lst.append(Node(21))
    lst.append(Node(22))
    lst.append(Node(23))
    lst.append(Node(24))
    print(lst)
    weaved = weave(lst)
    print(weaved)

    lst = SinglyLinkedList(head=Node(1))
    lst.append(Node(2))
    lst.append(Node(3))
    lst.append(Node(1))
    lst.append(Node(2))
    lst.append(Node(4))
    lst.append(Node(4))
    print(lst)
    nodups = remove_dups1(lst)
    print(nodups)
    kth = kth_last(lst,2)
    print(kth)
    kth = kth_last2(lst,2)
    print(kth)


    

