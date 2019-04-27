from typing import List
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

def is_subset_sum_rec(numbers, m):
    if m == 0:
        return True
    if m < 0:
        return False
    if len(numbers) == 0:
        return False
    return is_subset_sum_rec(numbers[1  :], m) or is_subset_sum_rec(numbers[  1:], m-numbers[0])

def is_subset_sum_dp(numbers, m):
    n = len(numbers)
    dp = [[False for i in range(m+1)] for i in range(n+1)]
    
    for i in range(n+1):
        for j in range(m+1):
            if j == 0:
                dp[i][j] = True
            elif i == 0:
                dp[i][j] = False
            elif j < numbers[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-numbers[i-1]]


    return dp[n][m]

def longest_snake(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    T = [[0 for i in range(n)] for j in range(m)]

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if i == m-1 and j == n-1:
                T[m-1][n-1] = grid[m-1][n-1]
            elif i == m-1:
                T[i][j] = grid[i][j] + T[i][j+1]
            elif j == n-1:
                T[i][j] = grid[i][j] + T[i+1][j]
            else:
                T[i][j] = grid[i][j] + max(T[i+1][j], T[i][j+1])
    
    return max(map(max, T))

def cutting_a_rod(rods) -> int:
    rods[0] = 0

    # Let T[i] be the maximum value obtained from a rod of length i.
    T = [0 for i in range(len(rods)+1)]
    T[0] = 0 

    # Either T[i] = max(rods[i], T[i-1] + rods[1], T[i-2] + rods[2]...)
    for i in range(1, len(T)):
        T[i] = max([rods[j] + T[i-j] for j in range(i)])

    return T[-1]

def knapsack_problem(values, weights, W):
    assert(len(values) == len(weights))
    # For each item, either it is included in the maximum subset or it is not.
    # Therefore, there are two cases:
    # 1. Maximum value obtained by n-1 items and W weight (excl. n).
    # 2. Value of nth item + maximum value obtained by n-1 items and W minus 
    #    the weight of the nth item (incl. n).
    
    # D[i][j] = max value using i items in volume j.
    D = [[0 for i in range(W+1)] for j in range(len(values)+1)]

    for i in range(len(values)+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                D[i][j] = 0
            elif weights[i-1] > j:
                D[i][j] = D[i-1][j]
            else:
                D[i][j] = max(D[i-1][j], values[i-1] + D[i-1][j - weights[i-1]])

    return D[len(values)][W]

def longest_common_subsequence(A, B):
    m = len(A)
    n = len(B)

    D = [[0 for i in range(n+1)] for j in range(m+1)]

    # 0: UP
    # 1: LEFT
    # 2: UP-LEFT

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                D[i][j] = 0
            elif A[i-1] == B[j-1]:
                D[i][j] = D[i-1][j-1] + 1
            elif D[i-1][j] >= D[i][j-1]:
                D[i][j] = D[i-1][j]
            else:
                D[i][j] = D[i][j-1]

    index = D[m][n]
    i = m 
    j = n 
    while i > 0 and j > 0: 
  
        # If current character in X[] and Y are same, then 
        # current character is part of LCS 
        if A[i-1] == B[j-1]: 
            print(A[i-1], end='')
            i-=1
            j-=1
            index-=1
  
        # If not same, then find the larger of two and 
        # go in the direction of larger value 
        elif D[i-1][j] > D[i][j-1]: 
            i-=1
        else: 
            j-=1
  
    return D[m][n]

    

if __name__ == "__main__":
    A = "ABCDGH"
    B = "AEDFHR"
    # A = "AGGTAB"
    # B = "GXTXAYB"
    print(longest_common_subsequence(A, B))
    # values = [60, 100, 120]
    # weights = [10, 20 , 30]
    # W = 50
    # print(knapsack_problem(values, weights, W))
    # rods = {1: 1, 2: 5, 3: 8, 4: 9, 5: 10, 6: 17, 7: 17, 8: 20}
    # rods2 = {1: 3, 2: 5, 3: 8, 4: 9, 5: 10, 6: 17, 7: 17, 8: 20}
    # print(cutting_a_rod(rods2))
    # A = [[9, 6, 5, 2],
    #      [8, 7, 6, 5],
    #      [7, 3, 1, 6],
    #      [1, 1, 1, 7]]
    # print(longest_snake(A))
    # print(is_subset_sum_dp([1, 2, 3], 5))
    # print(is_subset_sum_dp([1, 2, 3], 6))
    # print(is_subset_sum_dp([1, 2, 3], 7))
    # print(is_subset_sum_dp([1, 2, 3], 9))
    # print(ised_fib(5))
    # print(ative_fib(5))
    # print(er_fib(5))
    # print(le_step(5))
    # print(iple_step_memo(5))
    # print(triple_step_iterative(5))
    # print(triple_step_better(5))
   # print(perms2("abc"))
