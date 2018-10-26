"""
Calculates number of trailing zeros on a factorial
"""

def n_zeros(n):
    c_5 = 0
    i = 5
    while n // i > 0:
        c_5 += n // i
        i *=5
    return c_5

if __name__ == "__main__":
    n = 10
    print(f"Number of zeros in {n}! is {n_zeros(n)}")
