class Node:
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Could implement without this wrapper
class SinglyLinkedList:

    def __init__(self, head=None):
        self.head = head
        self._size = 0
    
    def append(self, node):
        curr = self.head

        while curr != None:
            curr = curr.next

        curr.next = node

        self._size += 1

    def get(self, pos):
        if pos > size:
            raise IndexError("Out of range")

        curr = self.head

        for i in range(pos):
            if curr == None:
                raise IndexError("Out of range")
            curr = curr.next

        return curr

def weave(l):
    s = l.head
    f = l.head

    if l.size < 3:
        print("Too small!")
        return
    
    while f != None:
        f = f.next.next
        s = s.next

    # When f hits the end, s wil be at the midpoint
    # Move f back to the front, and weave them together

    

class TestLinkedList:
    def __init__(self):
        self.l = SinglyLinkedList(head=Node(1))

    def test_append(self):
        self.l.append(Node(3))
        self.l.append(Node(19))
        assert self._l.size = 3

    def test_get(self):
        assert self.l.get(2) == 19
        

    

