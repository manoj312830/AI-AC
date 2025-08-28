
# The function factr is intended to compute the factorial, but:
# 1. The base case for n==0 should return 1, not 0.
# 2. The recursive step should be n*factr(n-1), not n*factr(n-2).
# 3. The function is called with a string "5" instead of an integer 5.
# 4. There is no input validation for negative numbers or non-integers.
# Here is the corrected code:

def factr(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factr(n - 1)

print(factr(5))
