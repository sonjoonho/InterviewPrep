class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __repr__(self):
        return "Node: {}".format(self.value)

    # You don't really need setters and getters in python the same way as Java!
   
class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def __repr__(self):
        prev = self.head
        curr = self.head.next

        arr = []

        i = 0
        while i < self.size:
            arr.append(curr)
            prev = curr
            curr = curr.next
            i += 1

        return str([str(node) for node in arr])

    def append_to_tail(self, node):
        # Remember to set both next and prev!
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

        self.size += 1

        # Return True if the list has been modified
        return True

    def append_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        
        self.size +=1

        return True

    def get(self, index):
        if index >= self.size or index < 0:
            raise IndexError 

        
        prev = self.head
        curr = self.head.next

        i = 0
        while i < index:
            prev = curr
            curr = curr.next

            i += 1

        # You need to return prev and curr!
        return prev, curr

    def append(self, node, index):
        prev, curr = self.get(index)
        curr.next.prev = node
        
        node.next = curr.next
        node.prev = curr

        curr.next = node

        self.size += 1

        return True


    def delete(self, index):
        prev, curr = self.get(index)
        
        curr.next.prev = prev
        prev.next = curr.next

        self.size -=1

        # If you're implementing this in C or C++, remember to deallocate the Node
        return True

#    def weave(self):
#        if size % 2 != 0:
#            raise Exception("Size must be even")
#
#        p1 = self.head.next
#        p2 = self.head.next
#        
#        while p1.next.value is not None:
#            p1 = p1.next.next
#            p2 = p2.next 
#
#        # p1 is now at the end and p2 is at the midpoint
#        # now move p1 to the front and start weaving
#
#        p1 = self.head
#
#        # This is long....


if __name__ == "__main__":
    linkedlist = DoublyLinkedList()
    print(linkedlist)
    linkedlist.append_to_tail(Node(5)) # [5] 
    print(linkedlist)
    linkedlist.append_to_tail(Node(4)) # [5, 4]
    print(linkedlist)
    linkedlist.append_to_head(Node(10)) # [10, 5, 4]
    print(linkedlist)
    linkedlist.append_to_tail(Node("hi")) # [10, 5, 4, "hi"]
    print(linkedlist)

    _, val = linkedlist.get(0) # 10
    print(val)
    _, val = linkedlist.get(3) # "hi"
    print(val)
    
    linkedlist.delete(2) # [10, 5, "hi"]
    print(linkedlist)
    linkedlist.delete(0) # [5, "hi"]
    print(linkedlist)

    linkedlist.append(Node(300), 1) # [5, 300, "hi"]
    print(linkedlist)
    linkedlist.append(Node(-400), 0) # [-400, 5, 300, "hi"]
    print(linkedlist)
    linkedlist.append(Node(1000), 3) # [-400, 5, 300, "hi", 1000]
    print(linkedlist)
    linkedlist.append(Node("no"), 3) # [-400, 5, 300, "hi", 1000]
    print(linkedlist)


