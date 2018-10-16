"""Node class definition
"""
class BinaryNode():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

"""Definitions
Complete binary tree: 
    Every level is fully filled except for perhaps the last level. To the extent that the last level is filled, it is filled left to right
Full binary tree:
    Every node has either zero or two children. No node has only one child
"""

"""Example trees
"""

tree1 = BinaryNode(5, BinaryNode(3, BinaryNode(2), BinaryNode(8)), BinaryNode(12))


"""Recursive In-Order Traversal
Visit left branch, then current node, then right branch
"""

def recursive_in_order_traversal(node):
    if node != None:
        recursive_in_order_traversal(node.left)
        print(node.value)
        recursive_in_order_traversal(node.right)

"""Recursive Pre-Order Traversal
Visit current node, then child nodes
"""

def recursive_pre_order_traversal(node):
    if node != None:
        print(node.value)
        recursive_pre_order_traversal(node.left)
        recursive_pre_order_traversal(node.right)

"""Recursive Post-Order Traversal
Current node after its child nodes (post and pre order are opposites)
"""

def recursive_post_order_traversal(node):
    if node != None:
        recursive_post_order_traversal(node.left)
        recursive_post_order_traversal(node.right)
        print(node.value)

"""HEAPS
A min-heap is a *complete* binary tree where each node is smaller than its children
A max-heap is a *complete* binary tree where each node is larger than its children
This is often implemented with a list, where p is the index of the parent node, 2p+1 is the index of the left child, and 2p+2 is the index of the right child
(These can change depending on implemetation)
Priority queues can be implemented using heaps
"""

class MinHeap:
    def __init__(self, heap_list=[]):
        self.heap_list = heap_list
        self.size = 0

    def __repr__(self):
        return "Heap {}".format(self.heap_list)

    """Heap insert
    When we insert into a min heap, we start by inserting the element at the rightmost bottom (to maintain the complete tree property).
    Then we "fix" the tree by swapping the new element with its parents until we find an appropriate spot for the element.
    This takes O(log n) time.
    """

    def insert(self, value):
        self.heap_list.append(value)
        self._iterative_percolate_up(len(self.heap_list)-1)

    # def _recursive_percolate_up(self):
    #     parent =         

    def _iterative_percolate_up(self, child_index):
        child = child_index
        
        while child > 0:
            parent = (child - 1) // 2
            if self.heap_list[parent] > self.heap_list[child]:
                self.heap_list[parent], self.heap_list[child] = self.heap_list[child], self.heap_list[parent]
            
            child = parent

    """Extract minimum
    Remove the minimum element from the top and swap it with the last element in the heap, and then heapify from the root down by swapping with smaller child
    """

    def extract_minimum(self):
        minimum = self.heap_list[0]
        
        self.heap_list[0] = self.heap_list[len(self.heap_list)-1]
        self._iterative_heapify()

        return minimum

    def _iterative_heapify(self):
        parent = 0
        
        while 2*parent < len(self.heap_list):
            left_child = (parent * 2) + 1
            right_child = (parent * 2) + 2
            smaller_child = left_child

            if self.heap_list[left_child] > self.heap_list[right_child]:
                smaller_child = right_child

            if self.heap_list[parent] > self.heap_list[smaller_child]:
                self.heap_list[smaller_child], self.heap_list[parent] = self.heap_list[parent], self.heap_list[smaller_child]
            
            parent = smaller_child


        

    def get_size(self):
        return _size
"""Example heaps
"""

minheap1 = MinHeap([4, 50, 7, 55, 90, 87])


"""Notes on graph represenations
You can have an adjacency list or an adjacency matrix
Adjacency lists are generally better because you can easily iterate through all the neighours
With adjacency matrices, you need to iterate through all the nodes to find a node's neighbours
"""

class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes

class GraphNode:
    def __init__(self, value, adjacent=[], visited=False):
        self.value = value
        self.adjacent = adjancent
        self.visited = visited

"""Depth First Search

"""

def recursive_dfs(root):
    if root is None:
        return
    print(root.value)
    root.visited = True

    for n in root.adjacent:
        if not n.visited:
            recursive_dfs(n)

"""Breadth First Search
Uses a queue
"""

from queue import Queue

def iterative_bfs(root):
    queue = Queue()
    root.visited = True

    while not queue.empty():
        r = queue.get()
        r.visited = True
        print(r.value)
        for n in r.adjacent:
            if not n.visited:
                queue.put(n)


if __name__ == "__main__":
    recursive_in_order_traversal(tree1)
    print("\n")
    recursive_pre_order_traversal(tree1)
    print("\n")
    recursive_post_order_traversal(tree1)
    print("\n")
    print(minheap1) 
    print("Insert 3")
    minheap1.insert(3)
    print(minheap1) 
    print("Insert 10")
    minheap1.insert(10)
    print(minheap1) 
    print("Extract min")
    min1 = minheap1.extract_minimum()
    print(min1)
    print(minheap1) 

