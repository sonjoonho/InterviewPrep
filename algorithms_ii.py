import pytest
from typing import List
from queue import Queue

"""
Contains Python implementations of most algorithms encountered in the 2nd year
Algorithms II course at Imperial College London.
"""

"""
DYNAMIC PROGRAMMING
"""

"""
Quicksort
"""
def super_speedy_sort(arr, p, r):
    # p is the beginning of the array, r is the end
    if p < r:
        q = partition(arr, p, r)
        # At this point, arr has been partitioned around the pivot
        super_speedy_sort(arr, p, q-1)
        super_speedy_sort(arr, q+1, r)

def partition(arr, p, r):
    # Select arr[r] as the pivot element
    x = arr[r]
    i = p - 1

    # Region p to i is the region less than the pivot
    # Region i to j is the regin greater than the pivot
    
    for j in range(p, r):
        if arr[j] <= x:
            i = i+1
            swap(arr, i, j)
    swap(arr, i+1, r)

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


"""
Maximum Subarray Sum
"""
def max_subarray_dp(arr):
    max_so_far = -1000
    max_ending_here = 0

    for i in range(len(arr)):
        max_ending_here += arr[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far

"""
Rod cutting
"""
def cutting_a_rod(rods: List[int]) -> int:
    # A rod of length 0 is worth nothing.
    rods[0] = 0

    # Let T[i] be the maximum value obtained from a rod of length i.
    T = [0 for i in range(len(rods)+1)]

    # Either T[i] = max(rods[i], T[i-1] + rods[1], T[i-2] + rods[2]...)
    for i in range(1, len(T)):
        T[i] = max([rods[j] + T[i-j] for j in range(i)])

    return T[-1]

"""
0/1 Knapsack problem
"""
def zero_one_knapsack_problem(values, weights, W):
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

"""
Longest Common Subsequence

Calculates the longest common subsequence between two strings.
"""
def longest_common_subsequence(A, B):
    m = len(A)
    n = len(B)

    D = [[0 for i in range(n+1)] for j in range(m+1)]

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

    print(print_lcs(D, A, B))
  
    return D[m][n]

"""
Prints the longest common subsequence using the DP table calculated above.

dab lol
"""
def print_lcs(D, A, B):
    m = len(A)
    n = len(B)

    index = D[m][n]

    result = [' ' for i in range(index)]

    i = m 
    j = n 
    while i > 0 and j > 0: 
  
        # If current character in X and Y are same, then 
        # current character is part of LCS 
        if A[i-1] == B[j-1]: 
            result[index-1] = A[i-1]
            i-=1
            j-=1
            index-=1
  
        # If not same, then find the larger of two and 
        # go in the direction of larger value 
        elif D[i-1][j] > D[i][j-1]: 
            i-=1
        else: 
            j-=1

    return "".join(result)

"""
Longest Common Subsequence of three strings

Simple extension of LCS.
"""

def longest_common_subsequence_of_three_strings(A, B, C):
    a = len(A)
    b = len(B)
    c = len(C)

    D = [[[0 for k in range(c+1)] for j in range(b+1)] for i in range(a+1)]

    for i in range(a+1):
        for j in range(b+1):
            for k in range(c+1):
                if i == 0 or j == 0 or j == 0:
                    D[i][j][k] = 0
                elif A[i-1] == B[j-1] == C[k-1]:
                    D[i][j][k] = D[i-1][j-1][k-1] + 1
                else:
                    D[i][j][k] = max(D[i-1][j][k],
                                     D[i][j-1][k],
                                     D[i][j][k-1])

    return D[a][b][c] 

def longest_common_palindromic_subsequence(s):
    s_r = s[::-1]

    return longest_common_subsequence(s, s_r)

"""
Longest snake

Longest path in a grid (similar to max_apples which 
appeared in a past paper.
"""
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

"""
Is Subset Sum

Simple recursive implementation.
"""
def is_subset_sum_rec(numbers: List[int], m: int):
    if m == 0:
        return True
    if m < 0:
        return False
    if len(numbers) == 0:
        return False
    return is_subset_sum_rec(numbers[1  :], m) or is_subset_sum_rec(numbers[  1:], m-numbers[0])

"""
Is Subset Sum

Bottom-up dynamic programming solution.
"""
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



"""
GREEDY ALGORITHMS
"""

"""
Fractional Knapsack Problem
"""
def fractional_knapsack_problem(values: List[int], weights: List[int], W: int) -> int:
    # Calculate the value per unit weight.
    value_per_weight = [v / w for (v, w) in zip(values, weights)][::-1]

    # Sort and reindex values and weights (I think you can just state this as
    # an assumption in the exam.
    values = [v for _, v in sorted(zip(value_per_weight, values), key = lambda pair: pair[0])]
    weights = [w for _, w in sorted(zip(value_per_weight, weights), key = lambda pair: pair[0])]

    remaining_weight = W
    max_val = 0
    i = 0
    while remaining_weight >= 0 and i < len(value_per_weight):
        # Determine how much we should take.
        t = min(1, remaining_weight / weights[i]) 

        max_val += t * values[i]
        remaining_weight -= t * weights[i]

        i += 1

    return max_val

"""
GRAPH ALGORTIHMS
"""

"""
Notes on graph represenations
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

"""
Depth First Search

Recursive implementation is generally easiest, but can be implemented
iteratively using a stack.
"""
def recursive_dfs(root):
    if root is None:
        return
    print(root.value)
    root.visited = True

    for n in root.adjacent:
        if not n.visited:
            recursive_dfs(n)

"""
Breadth First Search

Uses a queue.
"""
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

#def bellman_ford():

"""
Get Closest Number

Uses binary search for O(n log n) runtime.
"""
def closest_number(arr: List[int], n: int) -> int:

    low = 0
    high = len(arr)

    if n <= arr[0]:
        return arr[0]
    elif n >= arr[-1]:
        return arr[-1]

    while low < high:
        mid = (low + high) // 2
        
        if arr[mid] == n:
            return n

        elif n < arr[mid]:
            # Search left

            if mid > 0 and n > arr[mid-1]:
                return get_closest(arr[mid-1], arr[mid], n)

            high = mid
        else:
            if mid < n-1 and n < arr[mid+1]:
                return get_closest(arr[mid+1], arr[mid], n)
            low = mid+1


    return arr[mid]

def get_closest(a, b, n):
    return a if abs(n - a) < abs(n-b) else b

"""
DIVIDE AND CONQUER
"""

"""
Maximum Sum Subarray

1. Divide the array into two halves
2. Return max of
    a. Maximum subarray of left half
    b. Maximum subarray of right half
    c. Maximum subarray of mid
"""
def max_subarray_dc(arr, low, high):

    # Base case
    if (low == high):
        return arr[low]

    mid = (low + high) // 2

    # Max of three cases
    return max(max_subarray_dc(arr, low, mid),
               max_subarray_dc(arr, mid+1 ,high),
               max_crossing_sum(arr, low, mid, high))

def max_crossing_sum(arr, low, mid, high):
    total = 0
    left_total = -10000

    for i in range(mid, low-1, -1):
        total += arr[i]

        if total > left_total:
            left_total = total

    total = 0
    right_total = -10000

    for i in range(mid+1, high+1):
        total += arr[i]

        if total > right_total:
            right_total = total

    return left_total + right_total


class TestAlgorithmsII:
    def test_rod_cutting_1(self):

        rods = {1: 1, 2: 5, 3: 8, 4: 9, 5: 10, 6: 17, 7: 17, 8: 20}
        assert cutting_a_rod(rods) == 22

    def test_rod_cutting_2(self):
        rods = {1: 3, 2: 5, 3: 8, 4: 9, 5: 10, 6: 17, 7: 17, 8: 20}
        assert cutting_a_rod(rods) == 24

    def test_01_knapsack(self):
        values = [60, 100, 120]
        weights = [10, 20, 30]
        W = 50
        assert zero_one_knapsack_problem(values, weights, W) == 220

    def test_longest_common_subsequence_1(self):
        A = "ABCDGH"
        B = "AEDFHR"
        assert longest_common_subsequence(A, B) == 3

    def test_longest_common_subsequence_2(self):
        A = "AGGTAB"
        B = "GXTXAYB"
        assert longest_common_subsequence(A, B) == 4

    def test_longest_common_subsequence_of_three_strings_1(self):
        A = "geeks"
        B = "geeksfor"
        C = "geeksforgeeks"
        # bless geeks for geeks
        assert longest_common_subsequence_of_three_strings(A, B, C)

    def test_longest_common_subsequence_of_three_strings_1(self):
        A = "abcd1e2"
        B = "bc12ea"
        C = "bd1ea"
        # bless geeks for geeks
        assert longest_common_subsequence_of_three_strings(A, B, C)

    def test_longest_palindromic_subsequence(self):
        s = "CHARACTER"
        assert longest_common_palindromic_subsequence(s)
        
    def test_is_subset_sum_1(self):
        assert is_subset_sum_dp([1, 2, 3], 5) == True

    def test_is_subset_sum_2(self):
        assert is_subset_sum_dp([1, 2, 3], 6) == True

    def test_is_subset_sum_3(self):
        assert is_subset_sum_dp([1, 2, 3], 7) == False

    def test_is_subset_sum_4(self):
        assert is_subset_sum_dp([1, 2, 3], 9) == False

    def test_fractional_knapsack_problem(self):
        values = [60, 100, 120]
        weights = [10, 20, 30]
        W = 50
        assert fractional_knapsack_problem(values, weights, W) == 240

    def test_closest_number_1(self):
        arr = [1, 2, 4, 5, 6, 6, 8, 9]
        assert closest_number(arr, 11) == 9

    def test_closest_number_2(self):
        arr = [2, 5, 6, 7, 8, 8, 9]
        assert closest_number(arr, 4) == 5

    def test_maximum_subarray_dc(self):
        arr = [-2, -5, 6, -2, -3, 1, 5, -6]
        assert max_subarray_dc(arr, 0, len(arr)-1) == 7

    def test_maximum_subarray_dp(self):
        arr = [-2, -5, 6, -2, -3, 1, 5, -6]
        assert max_subarray_dp(arr) == 7


