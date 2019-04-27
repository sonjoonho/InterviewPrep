"""General Notes

Bottom up:
    Solve a simple case, figure out how to solve for a bigger case

Top down:
    Think about how we can divide the problem into N subproblems

To make a recursive algorithm into a dynamic programming algorithm, look for the overlapping sub problems and cache the

"""

def simple_recursive_fib(n):
    if i == 0:
        return 0
    if i == 1:
        return 1
    
    return fib(n-1) + fib(n-2)

""" 
The runtime of this function is O(2^n)
It helps to draw the recursion tree. This is a binary tree, and each node is O(1).
There are 2^n nodes in the binary tree so the total runtime is O(2^n)
(Actually it's slightly better because the left and right subtree are not the same size, it's closer to O(1.6^n))
"""

def memoised_fib(n):
    mem = [0] * (n+1)

    return memoised_fib_helper(n, mem)

def memoised_fib_helper(n, mem):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if mem[n] == 0:
        mem[n] = memoised_fib_helper(n-1, mem) + memoised_fib_helper(n-2, mem)

    return mem[n]

"""
The memoised version runs in O(n) time
"""

def iterative_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    memo = [0] * (n+1)
    memo[1] = 1

    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[n]

def better_fib(n):
    if n == 0:
        return 0
    
    a = 0
    b = 1

    for i in range(2, n):
        c = a + b
        a = b
        b = c

    return a+b

def triple_step(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    
    return triple_step(n-1) + triple_step(n-2) + triple_step(n-3)

def triple_step_memo(n):
    memo = [0] * (n+1)

    return triple_step_memo_helper(n, memo)

def triple_step_memo_helper(n, memo):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if memo[n] == 0:
        memo[n] = triple_step_memo_helper(n-1, memo) + triple_step_memo_helper(n-2, memo) + triple_step_memo_helper(n-3, memo)

    return memo[n]

def triple_step_iterative(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    
    memo = [0] * (n+1)
    memo[0] = 1
    memo[1] = 1
    memo[2] = 2

    for i in range(3, n):
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]

    return memo[n-1] + memo[n-2] + memo[n-3]

def triple_step_better(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    
    a = 1
    b = 1
    c = 2

    for i in range(3, n):
        d = a + b + c
        a = b
        b = c
        c = d

    return a + b + c

"""
8.4 Power set
"""
def power_set(l):
    # The power set of the empty set is the set containign the empty set
    if l == []:
        return [[]]
    # The power set of any other set is the power set of the set containing
    # some element, and all without
    e = [l[0]]
    rest = power_set(l[1:])
    return rest + [e + y for y in rest]

#broken
def power_set2(l):
    # Count up to 2^len(l) in binary, masking as we go
    ps = []
    bitmask = [0] * 2**len(l)
    for k in range(2**len(l)):
        for i, c in enumerate(str(bin(k))[2:]):
            bitmask[i] = int(c)
        print(bitmask)
        ps.append([x for x, k in zip(l, bitmask) if k == 1])
    return ps

"""
8.7 Permuations with Dups
"""

"""
takes a string
return an array of strings
"""
def perms(s):
    permutations = []

    if s == "":
        permutations.append("")
        return permutations

    x = s[0]
    xs = s[1:]
    words = perms(xs)
    for word in words:
        for i in range(len(word)+1):
            s = word[:i] + x + word[i:]
            print(s)
            permutations.append(s)
    return permutations

def perms2(s):
    if s == "":
        return [""]

    permutations = []
    
    for i in range(len(s)):
        p = perms(s[:i] + s[i+1:])
        for word in p:
            permutations.append(s[i] + word)
    return permutations

"""
Robot in a Grid
"""
def get_path(maze):
    if maze is None:
        print("Maze is empty")
        return None

    path = []
    find_path(maze, (len(maze)-1, len(maze[0])-1), path)
    return path

def path(maze, point, path):
    r = point[0]
    c = point[1]

    if r < 0 or c < 0 or not maze[r][c]:
        return False

    if path(maze, (r-1, c), path) or path(maze, (r, c-1), path):
        path.append((r, c))
        return True
    return False

def count_paths(maze, r, c, count):
    if maze[r][c] == None:
        return 0
    if r == len(maze) and c == len(maze[0]):
        return 1
    
    return count_paths(maze, r+1, c) + count_paths(maze, r, c) 

def count_paths_mem(maze, r, c, paths):
    if maze[r][c] == None:
        return 0
    if r == len(maze) and c == len(maze[0]):
        return 1
    
    paths[r][c] = count_paths_mem(maze, r+1, c, paths) + count_paths_mem(maze, r, c+1, paths)
    return paths[r][c]
    

if __name__ == "__main__":
    # print(memoised_fib(5))
    # print(iterative_fib(5))
    # print(better_fib(5))
    # print(triple_step(5))
    # print(triple_step_memo(5))
    # print(triple_step_iterative(5))
    # print(triple_step_better(5))
    # print(perms2("abc"))
