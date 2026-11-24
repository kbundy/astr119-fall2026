#------------------------------------------------------------------------------
# This module defines multitab() a multiplication table generator.
#------------------------------------------------------------------------------
import math

def multitab(n):
    """Print multiplication table up to n.

    Parameters
    ----------
    n : positive integer scalar

    Returns
    -------
    None
    """
    
    assert (type(n) is int) and (n > 0), "n must be positive integer"

    w = int(math.log10(n**2)) + 1   # calculates the width the collumns must be to avoid drift
    for k in range(1, n+1):
            for i in range(1, n+1):
                print(f"{k*i:>{w}}", end=' ')
            print()

    return None

### To run as a utility
if __name__ == '__main__':
    n = int(input("Multiplication table size: "))
    multitab(n)
