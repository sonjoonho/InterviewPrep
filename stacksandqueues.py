class Stack:
    def __init__(self, stack=[]):
        self.stack = stack

    def pop(self):
        # Get last element
        #val = self.stack[-1]
        # Remove last element
        #self.stack = stack[:-1]

        # Python lists have a pop method, but that's probably not what you're looking for
        return stack.pop()

    def push(self, val):
        self.stack.append(val)

    def peek(self):
        return self.stack[-1]

    def isempty(self):
        return self.stack.isempty()

# Also can be implemented using a singly linked list!!
# So can queues. Heaps can be used to implement a PRORITY queue
# Stacks and queues are pretty much the same thing, just add and remove at different ends

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack():
    def __init__(self):
        self.top = None

    def pop(self):
        if self.top is None:
            raise Exception("Stack is empty")

        item = self.top.value
        self.top = self.top.next

        return item

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def peek(self):
        return self.top

    def isempty(self):
        return self.top is None
        
class Queue():
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, value):
        node = Node(value)
        if self.last is not None:
            self.last.next = node

        self.last = node

        if self.first is None:
            self.first = self.last

    def remove(self):
        if self.first is None:
            raise Exception("Queue is empty")

        item = self.first.value
        self.first = self.first.next

        return item

    def peek(self):
        if self.first is None:
            raise Exception("Queue is empty")

        return self.first.value

    def isempty(self):
        return self.first is None

if __name__ == "__main__":
    stack = Stack()
    stack.push(5)
    stack.push(3)
    stack.push(8)
    stack.push(0)

    v = stack.pop()
    print(v)
    v = stack.pop()
    print(v)
    v = stack.pop()
    print(v)
    v = stack.pop()
    print(v)
    
    queue = Queue()
    queue.add(5)
    queue.add(3)
    queue.add(8)
    queue.add(0)

    v = queue.remove()
    print(v)
    v = queue.remove()
    print(v)
    v = queue.remove()
    print(v)
    v = queue.remove()
    print(v)

