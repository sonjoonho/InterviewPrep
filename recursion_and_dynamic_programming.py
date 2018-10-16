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
    


if __name__ == "__main__":
    # print(memoised_fib(5))
    # print(iterative_fib(5))
    # print(better_fib(5))
    print(triple_step(5))
    print(triple_step_memo(5))
    print(triple_step_iterative(5))
    print(triple_step_better(5))
