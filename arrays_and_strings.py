import pytest

"""
1.1 isUnique

Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""
def isUnique(s):
    """
    This solution uses a bit map as a set. We cold also check if the length
    of the string is greater than the length of the ASCII character set. This
    isn't done here because it could be Unicode.

    Time complexity: O(n)
    Space complexity: O(1)
    """
    checker = 0
    for c in s:
        val = ord(c) - ord('a')
        if (checker & (1 << val)) > 0:
            return False
        else:
            checker |= 1 << val
    return True

def isUnique2(s):
    """
    If we cannot use additional data structures, we can check every character
    against every other character

    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    for a in range(len(s)):
        for b in range(a+1, len(s)):
            if s[a] == s[b]:
                return False
    return True

def isUnique3(s):
    """
    Or, sort the string and check that no neighbouring characters are the same

    Time complexity: O(nlog(n))
    Space complexity: Depends on sorting algorithm
    """
    s = sorted(s)
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False
    return True

def isUnique4(s):
    """ 
    A more pythonic way (not for use in interview)
    """
    return len(s) == len(set(s))

"""
1.2 Check Permutation

Given two strings, write a method to decide if one is permutation of the
other.
"""

def checkPermutation(a, b):
    """
    We count the occurences and store them in a map. Then compare the maps.

    Time complexity: O(n)
    Space complexiy: O(n)
    """
    if len(a) != len(b):
        return False

    mapa = {}
    mapb = {}
    
    for (c, d) in zip(a, b):
        mapa[c] = mapa[c] + 1 if c in mapa else 1
        mapb[d] = mapb[d] + 1 if d in mapb else 1
    
    return mapa == mapb        

def checkPermutation2(a, b):
    """
    Sort each string and compare

    Time complexity: O(nlog(n))
    Space complexity: O(1)
    """
    return sorted(a) == sorted(b)

def checkPermutation3(a, b):
    """
    Check character counts, but using an array instead of a dict/hashtable
    """
    if len(a) != len(b):
        return False

    letters = [0]*128 # Assumption: ASCII

    for c in a:
        letters[ord(c)] += 1

    for c in b:
        letters[ord(c)] -= 1
        if letters[ord(c)] < 0:
            return False

    # Since letters sums to 0, if there are no negative values then there
    # cannot be any positive values
    return True

"""
1.3 URLify

Replace all spaces in a string with '%20'. Assume that the string has
sufficient space at the end to hold additional characters. You are given
the true length of the string. Perform this in place.
"""

def URLify(s, n):
    """
    Each time a space is encountered, shift remaining characters by 2 and
    replace the space wih %20

    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    s = list(s)
    for i in range(len(s)):
        if s[i] == ' ':
            for j in range(len(s)-1, i, -1):
                s[j] = s[j-1]
            for j in range(len(s)-1, i, -1):
                s[j] = s[j-1]


            s[i] = '%'
            s[i+1] = '2'
            s[i+2] = '0'

    return "".join(s)

def URLify2(s, n):
    """
    Two passes. First pass counts the number of spaces to calculate how many
    extra characters we need. Second pass we edit the string. If we see a 
    space, replace it with '%20'. Else, copy the original character.
    """
    s = list(s)

    spaces = 0
    for i in range(n):
        if s[i] == ' ':
            spaces += 1

    index = n + spaces*2
    
    for i in range(n-1, 0, -1):
        if s[i] == ' ':
            s[index-1] = '0'
            s[index-2] = '2'
            s[index-3] = '%'
            index -= 3
        else:
           s[index - 1] = s[i]
           index -= 1
        
    return "".join(s)

"""
1.4 Palindrome Permutation

Write a function to check if a string is a permuation of a palindrome.
"""
def palindromePermutation(s):
    """ 
    In a palindrome, the number of characters with an odd count can at
    max be 1.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    s = s.lower().replace(' ','')
    
    counts = {}
    for c in s:
        counts[c] = counts[c] + 1 if c in counts else 1

    found_odd = False
    for (k, v) in counts.iteritems():
        if v % 2 == 1: # If the count is odd
            if found_odd: # And we have already found one odd
                return False
            found_odd = True
        
    return True
            
def palindromePermutation2(s):
    """ 
    The same, but check odds as you go along. Not necessarily better.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    s = s.lower().replace(' ','')
    
    odds = 0
    counts = {}
    for c in s:
        counts[c] = counts[c] + 1 if c in counts else 1
        if counts[c] % 2 == 1:
            odds += 1
        else:
            odds -= 1

    return not odds > 1

def palindromePermutation3(s):
    """
    The same, but use a bit vector

    Time complexity: O(n)
    Space complexity: O(1)
    """
    s = s.lower().replace(' ','')

    bitVector = createBitVector(s)

    return bitVector == 0 or checkExactlyOneBitSet(bitVector)

def createBitVector(s):
    bitVector = 0
    for c in s:
        x = ord(c) - ord('a')
        mask = 1 << x
        bitVector ^= mask

    return bitVector

def checkExactlyOneBitSet(bitVector):
    return bitVector - 1 & bitVector == 0



"""
1.5 One Away

There are three types of edits that can be performed on strings: insert, 
remove, or replace. Given two strings, write a function to check if they
are one edit or less away.
"""

def oneAway(a, b):
    """ 
    Time complexity: O(n)
    """

    if len(a) == len(b):
        return oneEditReplace(a, b)
    elif len(a) + 1 == len(b):
        # b > a
        return oneEditRemove(b, a)
    elif len(a) == len(b) + 1:
        # a > b
        return oneEditRemove(a, b)
    return False

def oneEditReplace(a, b):
    # Check if the strings differ in more than one place
    found_diff = False
    for i in range(len(a)):
        if a[i] != b[i]:
            if found_diff:
                return False
            else:
                found_diff = True
    return True

def oneEditRemove(a, b):
    # Check if you can remove one character from a to make b
    # Pre: len(a) > len(b)
    for i in range(len(a)):
        if a[:i] + a[i+1:] == b:
            return True
    return False

"""
1.6 String Compression

Perform basic string compression using the counts of repeated characters.
Assume only a-z as input.
"""

def stringCompression(s):
    """
    Naive implemetation. Slow because string concatenation operates in O(n^2)

    Time complexity: O(p + k^2) where p is the length of the original string
    and k is the number of character sequences.
    """
    r = ""
    count = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            r += s[i] + str(count)
            count = 1

    r += s[i] + str(count)

    return r if len(r) < len(s) else s
    
def stringCompression2(s):
    """
    Can speed up using StringBuilding in Java, or lists in Python. List
    comprehensions are the fastest but not always possible.
    """
    r = []
    count = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            r.append((s[i], count))
            count = 1
    
    r.append((s[i], count))
    compressed_string = "".join(e for e in ["".join([str(c) for c in lst]) for lst in r])
    return compressed_string if len(compressed_string) < len(s) else s

"""
1.7 Rotate Matrix

Given an NxN matrix, wrote a method to rotate the image by 90 degrees. Can
you do this in place?
"""

def rotateMatrix(m):
    """
    Element wise.

    Time complexity: O(n^2)
    Space complexity: O(n^2)
    """
    n = [x[:] for x in m]
    for i in range(len(m)):
        for j in range(len(m)):
            newi = j
            newj = len(m) - 1 - i
            n[newi][newj] = m[i][j]
    return n 

def rotateMatrix2(m):
    """
    Proceed layer by layer, performing a circular rotation. Performed in place.

    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    for layer in range(len(m)/2):
        first = layer
        last = len(m) - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = m[first][i] # save top
            m[first][i] = m[last-offset][first] # left -> top
            m[last-offset][first] = m[last][last-offset] # botton -> left
            m[last][last-offset] = m[i][last] # right to bottom
            m[i][last] = top # top -> right

    return m

"""
1.8 Zero Matrix

Write an algorithm such that if an element in an MxN matrix is 0, its entire
row and column are set to 0
"""

def zeroMatrix(matrix):
    """
    We use arrays to keep track of which rows and columns need
    to be nullified, and perform two passes.

    Time complexity: O(m*n)
    Space compexity: O(max(m, n))
    """
    m = len(matrix)
    n = len(matrix[0])

    rows = []
    cols = []
    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                rows.append(row)
                cols.append(col)

    for row in rows:
        for col in range(n):
            matrix[row][col] = 0

    for row in range(m):
        for col in cols:
            matrix[row][col] = 0

    return matrix

def zeroMatrix2(matrix):
    """
    We can improve on this by using the first row and first column as rows and cols

    Time complexity: O(n*m)
    Space complexity: O(1)
    """

    n = len(matrix)
    m = len(matrix[0])

    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                matrix[row][0] = 0
                matrix[0][col] = 0

    for row in range(n):
        if matrix[row][0] == 0:
            matrix[row] = [0] * m
        if matrix[0][col] == 0:
            matrix[row][col] = 0

    return matrix

def longest_palindromic_subsequence(s: str) -> int:
    s_r = s[::-1]

    return longest_common_subsequence(s, s_r) 

def longest_common_subsequence(a, b):
    
    L = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]

    for i in range(len(a)+1):
        for j in range(len(b)+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif a[i-1] == b[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    return L[len(a)][len(b)]

class TestArraysAndStrings:
    def test_isUnique(self):
        s = "abcdefg"
        assert isUnique(s)
        assert isUnique2(s)
        assert isUnique3(s)
        assert isUnique4(s)
        s = "abcdefga"
        assert not isUnique(s)
        assert not isUnique2(s)
        assert not isUnique3(s)
        assert not isUnique4(s)

    def test_checkPermutation(self):
        a = "abc"
        b = "bca"
        assert checkPermutation(a, b)
        assert checkPermutation2(a, b)
        assert checkPermutation3(a, b)
        a = "abcd"
        b = "bca"
        assert not checkPermutation(a, b)
        assert not checkPermutation2(a, b)
        assert not checkPermutation3(a, b)
        a = "adc"
        b = "bca"
        assert not checkPermutation(a, b)
        assert not checkPermutation2(a, b)
        assert not checkPermutation3(a, b)

    def test_URLify(self):
        i = ("Mr John Smith    ", 13)
        o = "Mr%20John%20Smith"
        assert URLify(i[0], i[1]) == o
        assert URLify2(i[0], i[1]) == o
        
#    def test_palindromePermutation(self):
#        s = "tact coa"
#        assert palindromePermutation(s)
#        assert palindromePermutation2(s)
#        assert palindromePermutation3(s)
#        s = "tactldcoa"
#        assert not palindromePermutation(s)
#        assert not palindromePermutation2(s)
#        assert not palindromePermutation3(s)

    def test_oneAway(self):
        s = ("pale", "ple")
        assert oneAway(s[0], s[1])
        s = ("pales", "pale")
        assert oneAway(s[0], s[1])
        s = ("pale", "bale")
        assert oneAway(s[0], s[1])
        s = ("pal", "pale")
        assert oneAway(s[0], s[1])
        s = ("pale", "bake")
        assert not oneAway(s[0], s[1])
        s = ("pale", "fdhsjbake")
        assert not oneAway(s[0], s[1])

    def test_stringCompression(self):
        s = "aabcccccaaa"
        assert stringCompression(s) == "a2b1c5a3"
        assert stringCompression2(s) == "a2b1c5a3"

#    def test_rotateMatrix(self):
#        m = [[1, 2, 3],
#             [4, 5, 6],
#             [7, 8, 9]]
#        assert rotateMatrix(m) == [[7, 4, 1],
#                                   [8, 5, 2],
#                                   [9, 6, 3]]
#        assert rotateMatrix2(m) == [[7, 4, 1],
#                                   [8, 5, 2],
#                                   [9, 6, 3]]
#    def test_zeroMatrix(self):
#        m = [[1, 0, 3],
#             [4, 5, 6],
#             [7, 8, 9]]
#        assert zeroMatrix(m) == [[0, 0, 0],
#                                 [4, 0, 6],
#                                 [7, 0, 9]]
#        assert zeroMatrix2(m) == [[0, 0, 0],
#                                 [4, 0, 6],
#                                 [7, 0, 9]]
#

    def test_longest_palindromic_subsequence(self):
        assert longest_palindromic_subsequence("nkoonj") == 4
