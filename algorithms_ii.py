import pytest
from typing import List

"""
Contains Python implementations of all algorithms encountered in the 2nd year
Algorithms II course at Imperial College London.
"""

"""
Dynamic Programming.
"""

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

    print_lcs(D, A, B)
  
    return D[m][n]

"""
Prints the longest common subsequence using the DP table calculated above.

dab lol
"""
def print_lcs(D, A, B):
    m = len(A)
    n = len(B)

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

"""
Longest snake

Longest path in a grid (similar to max_apples which 
appeard in a past paper.
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

