"""
We use a bottom-up dynamic programmming approach.
"""
def longest_common_substring(word1: str, word2: str) -> int:
    # Store length of current longest substring
    current_length = 0

    # Initialise memo table
    memo = [[0 for i in range(len(word2))] for j in range(len(word1))]

    for i in range(0, len(word1)):
        for j in range(0, len(word2)):
            if word1[i] == word2[j]:
            # Case 1: 
                memo[i][j] = memo[i-1][j-1] + 1
            else:
            # Case 2:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])
                
            current_length = memo[i][j]

    return current_length 

def longest_common_substring_rec(word1: str, word2: str) -> str:
    return longest_common_substring_rec_aux(word1, word2, len(word1)-1, len(word2)-1)

def longest_common_substring_rec_aux(word1: str, word2: str, m: int, n: int) -> str:
    if m < 0 or n < 0:
        return ""

    if word1[m] == word2[n]:
        return longest_common_substring_rec_aux(word1, word2, m-1, n-1) + word1[m]
    else:
        lcs1 = longest_common_substring_rec_aux(word1, word2, m-1, n)
        lcs2 = longest_common_substring_rec_aux(word1, word2, m, n-1)
        if len(lcs1) > len(lcs2):
            return lcs1
        else:
            return lcs2


"""
LEV-DISTANCE(X,Y)
1: m = X.length
2: n = Y.length
3: let d[0..m,0..n] be new table
4: for i = 1 to m
5:  d[i,0] = i
6: for j = 0 to n
7:  d[0,j] = j
8: for j = 1 to n
9:  for i = 1 to m
10:  c = xi == yj ? 0 : 1
11:  d[i,j] = min(d[i-1,j] + 1, d[i,j-1] + 1, d[i-1,j-1] + c)
12: return d[m,n]
"""
#def lev_distance(word1: str, word2: str):
#    m = len(word1)
#    n = len(word2)
#
#    d = [[0 for i in range(len(word2))] for j in range(len(word1))]
#    for i in range(1, m+1):
#        d[i][0] = i 
#    for j in range(1, n+1)
#        d[0][j] = j
#    for 


if __name__ == "__main__":
    print(longest_common_substring_rec("abzzzc", "abc"))
